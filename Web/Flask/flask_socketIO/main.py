import json
import eventlet
from threading import Lock
from flask import Flask, render_template, session, \
    copy_current_request_context, request
from flask_socketio import SocketIO, emit, disconnect

"""导入自定义包"""
from tools import connect_db
from tools import handle_data
from config import Config

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None
eventlet.monkey_patch()
thread_lock = Lock()
thread = None

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
socketio = SocketIO(app, async_mode=async_mode)

"""自定义全局变量"""
worker = None
redisObj = None  # redis连接对象
reconnectionCount = 0  # 重连次数
retrySwitch = False  # 重试开关
alreadySendDataList = []  # 存储已发送的数据
breakPosition = {'key': '', 'index': 0}  # 中断发送时数据停留位置（目前重连之后还是从第一条开始发送）
speed = 0  # 速率


class TqWebSocket(object):
    count = 0  # 统计服务端自动发送数据条数

    def __init__(self, socketIO):
        self.socketio = socketIO  # socketIO 对象
        self.sendSwitch = False  # 发送消息开关
        self.keyList = []  # 存储redis db0所有键数据
        self.scoreList = []  # 存储flag score数据
        self.recordsList = []  # 存储records数据
        self.startTime = (1609045821 - 60)  # 开始时间用于计算第一条数据的时间间隔(第一条攻击数据的时间戳-60s)

    def auto_creat_task(self):
        """自动创建并行任务"""
        for key in self.keyList:
            self.socketio.start_background_task(target=self.auto_send_attack_message, key=key)
        self.socketio.start_background_task(target=self.auto_send_team_score)
        self.socketio.start_background_task(target=self.auto_send_flag_records)

    def auto_send_attack_message(self, key):
        """自动推送消息"""
        time_interval = handle_data.first_attack_time_interval(self.startTime, key, speed)  # 初始时间间隔
        while self.sendSwitch:
            data_list = redisObj.zrange(key, 0, -1)
            for i in range(len(data_list)):
                # 过滤掉MIX前面9条时间间隔与其他队伍相差太多的数据
                if key == 'MIX' and i < 9:
                    continue

                # 下条记录的时间间隔
                self.socketio.emit('time_internal',
                                   {'data': f'The next data of team - {key} time interval: {time_interval} s'})
                # 暂停
                eventlet.sleep(time_interval)
                # 发送开关关闭就跳出
                if not self.sendSwitch:
                    return

                # 计算时间间隔
                now_data = data_list[i]
                try:
                    print('now speed:', speed)
                    next_data = data_list[i + 1]
                    time_interval = handle_data.calculate_time_interval(now_data, next_data, speed)
                except IndexError as e:
                    print('team: %s,没有下条数据了---' % key, e)

                # 处理数据
                string_data = handle_data.replace_time(data_list[i])
                self.socketio.emit('server_response',
                                   {'data': string_data, 'count': self.count})

                # 轮询完数据就跳出
                if i == len(data_list) - 1:
                    return
                self.count += 1
            eventlet.sleep(1)

    def auto_send_team_score(self):
        """自动推送team score"""
        time_interval = handle_data.first_score_time_interval(self.startTime, speed)  # 初始时间间隔
        while self.sendSwitch:
            data_list = self.scoreList
            for i in range(len(data_list)):
                # 下条记录的时间间隔
                self.socketio.emit('time_internal',
                                   {'data': f'The next team score time interval: {time_interval} s'})
                # 暂停
                eventlet.sleep(time_interval)
                # 发送开关关闭就跳出
                if not self.sendSwitch:
                    return

                # 计算时间间隔
                now_data = data_list[i]['flagTime']
                try:
                    next_data = data_list[i + 1]['flagTime']
                    time_interval = handle_data.calculate_score_time_interval(now_data, next_data, speed)
                except IndexError as e:
                    print('score: 没有下条数据了---', e)

                # 处理数据
                string_data = handle_data.replace_score_time(data_list[i])
                self.socketio.emit('server_response',
                                   {'data': string_data, 'count': self.count})

                # 轮询完数据就跳出
                if i == len(data_list) - 1:
                    return
                self.count += 1
            eventlet.sleep(1)

    def auto_send_flag_records(self):
        """自动推送flag records记录"""
        time_interval = handle_data.first_flag_time_interval(self.startTime, speed)  # 初始时间间隔
        while self.sendSwitch:
            data_list = self.recordsList
            for i in range(len(data_list)):
                # 下条记录的时间间隔
                self.socketio.emit('time_internal',
                                   {'data': f'The next flag data time interval: {time_interval} s'})
                # 暂停
                eventlet.sleep(time_interval)
                # 发送开关关闭就跳出
                if not self.sendSwitch:
                    return

                # 计算时间间隔
                now_data = data_list[i]['data']['created_at']
                try:
                    next_data = data_list[i + 1]['data']['created_at']
                    time_interval = handle_data.calculate_score_time_interval(now_data, next_data, speed)
                except IndexError as e:
                    print('RECORDS: 没有下条数据了---', e)

                # 处理数据
                string_data = handle_data.replace_records_time(data_list[i])
                self.socketio.emit('server_response',
                                   {'data': string_data, 'count': self.count})

                # 轮询完数据就跳出
                if i == len(data_list) - 1:
                    return
                self.count += 1
            eventlet.sleep(1)


@socketio.event
def switch_speed(message):
    """推送中途改变速度"""
    global speed
    # 获取客户端传递过来的速率
    speed = int(message['speed'])


@socketio.event
def client_send_event(message):
    """接收客户端发送的消息"""
    if message['data'] == "ok":
        print('ok(speed: %s) - %s' % (message['speed'], handle_data.get_now_time()))
        global worker, redisObj, speed, thread
        # 获取redis对象
        redisObj = connect_db.connect_redis()
        # 获取客户端传递过来的速率
        speed = int(message['speed'])
        # 初始化数据
        worker.sendSwitch = True
        worker.scoreList = handle_data.get_score_data()
        worker.recordsList = handle_data.get_records_data()
        worker.keyList = redisObj.keys('*')

        # 创建后台子线程
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(worker.auto_creat_task)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('tip',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)

    # 关闭发送消息开关
    global worker, reconnectionCount, retrySwitch, thread
    thread = None
    # 关闭推送消息开关
    worker.sendSwitch = False
    # retrySwitch = True
    # reconnectionCount += 1


@socketio.event
def connect():
    global worker
    # 创建Socket连接实例
    worker = TqWebSocket(socketio)
    emit('tip', {'data': 'Connected', 'count': 0})
    print('Client connected - %s' % handle_data.get_now_time())


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, host=Config.WEB_SERVER_HOST, port=Config.WEB_SERVER_PORT)

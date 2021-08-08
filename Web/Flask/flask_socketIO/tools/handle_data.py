import time
import datetime
import json
from tools import connect_db


def time_interval(stamp1, stamp2):
    """时间戳转datetime再计算时间间隔"""
    t1 = time.localtime(stamp1)
    t2 = time.localtime(stamp2)
    t1 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", t2)
    time1 = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
    return (time2 - time1).seconds


def map_data(data, type_name):
    new_dict = {
        'data': data,
        'type': type_name
    }
    return new_dict


"""
处理attack data
"""


def calculate_time_interval(now_data, next_data, speed):
    """计算时间间隔"""
    if next_data == '':
        return 0
    else:
        # string转json
        json_now = json.loads(now_data)
        json_next = json.loads(next_data)
        # 得到时间戳
        now_time_stamp = json_now["data"]["create_time"]
        next_time_stamp = json_next["data"]["create_time"]
        result = (next_time_stamp - now_time_stamp) / speed
        return result


def get_now_time():
    """得到当前时间"""
    # 获取当前时间的时间戳
    now_time_stamp = int(time.time())
    # .localtime() 方法把时间戳转换为时间元组对象
    tuple_time = time.localtime(now_time_stamp)
    # 得到字符串时间
    string_date = time.strftime("%Y-%m-%d %H:%M:%S", tuple_time)
    return string_date


def replace_time(data):
    """处理数据"""
    # string转json
    json_data = json.loads(data)
    # 用当前时间替换原来的时间
    now_time = get_now_time()
    json_data['data']['create_time'] = now_time
    # json转string
    string_data = json.dumps(json_data, ensure_ascii=False)
    return string_data


def first_attack_time_interval(start_time, key, speed):
    redis_obj = connect_db.connect_redis()
    data = redis_obj.zrange(key, 0, 0)
    json_data = json.loads(data[0])
    first_time = json_data['data']['create_time']
    return (first_time - start_time) / speed


"""
处理team score
"""


def get_score_data():
    """得到分数数据"""
    redis_obj6 = connect_db.connect_redis_db6()
    data = redis_obj6.get('score')
    json_data = json.loads(data)
    json_data = json_data['score']['flagTime']

    data_list = []  # 存储最后结果
    stamp_list = []  # 存储未排序的时间戳

    # 时间戳从小到大排序
    for time_stamp in json_data:
        stamp_list.append(int(time_stamp))
    stamp_list.sort()

    # 把处理好的数据添加进 data_list
    for time_stamp in stamp_list:
        temp_dict = {
            'flagTime': 0,
            'team': dict
        }
        time_stamp //= 1000
        temp_dict['flagTime'] = time_stamp
        temp_dict['team'] = json_data[str(time_stamp * 1000)]
        data_list.append(temp_dict)
    return data_list


def calculate_score_time_interval(now_data, next_data, speed):
    """计算flag score的时间间隔"""
    return (int(next_data) - int(now_data)) / speed


def replace_score_time(json_data):
    """处理数据"""
    # 用当前时间替换原来的时间
    now_time = get_now_time()
    json_data['flagTime'] = now_time
    json_data = map_data(json_data, 'score')
    # json转string
    string_data = json.dumps(json_data, ensure_ascii=False)
    string_data = string_data.replace("'", '"')
    return string_data


def first_score_time_interval(start_time, speed):
    first_time = 1609045801
    return (first_time - start_time) / speed


"""
处理flag records
"""


def get_records_data():
    """得到records数据"""
    redis_obj6 = connect_db.connect_redis_db6()
    data = redis_obj6.get('RECORDS')
    json_data = json.loads(data)
    record_list = json_data['RECORDS']
    # print(record_list)
    return record_list


def replace_records_time(json_data):
    """处理数据"""
    # 用当前时间替换原来的时间
    now_time = get_now_time()
    json_data['data']['created_at'] = now_time
    # json转string
    string_data = json.dumps(json_data, ensure_ascii=False)
    string_data = string_data.replace("'", '"')
    return string_data


def first_flag_time_interval(start_time, speed):
    first_time = 1609047826
    return (first_time - start_time) / speed


if __name__ == '__main__':
    # get_records_data()
    first_fire_time = 1608691978
    first_flag_time = 1609047826
    first_score_time = 1609045801
    # first_attack_time_interval(1, 'MIX', 1)
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 8/2/2020 10:50 PM
# __software__ : PyCharm

from tkinter import *
from tkinter import messagebox

import socket
import threading
import time

import inspect
import ctypes

# import tkinter.scrolledtext as Scrolledtext
# from PublicClass.KillThread import stop_thread


'''杀死子线程'''
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

'''杀死子线程'''



class Server:
    # 初始化赋值
    def __init__(self, ):
        '''
        绘制窗体相关
        '''
        self.root = Tk()
        self.width = self.root.winfo_screenwidth()  # 获取电脑窗体的宽度
        self.height = self.root.winfo_screenheight()  # 获取电脑窗体的高度

        '''
        开启Socket服务相关
        '''
        self.host = ''  # target host
        self.port = ''  # target port

        self.initMain()
        self.root.mainloop()

    # 初始化主窗口
    def initMain(self):
        self.root.title('socket服务端')
        x = int((self.width - 320) / 2)  # x轴偏移量
        y = int((self.height - 90) / 2)  # x轴偏移量
        self.root.geometry('320x90+%s+%s' % (x, y))
        label1 = Label(self.root, text='设置Host:', padx=5)
        label1.grid(row=0, column=0, sticky=W)
        self.entry1 = Entry(self.root, width=40)
        self.entry1.grid(row=0, column=1, sticky=W, pady=5)

        label2 = Label(self.root, text='设置Port:', padx=5)
        label2.grid(row=1, column=0, sticky=W)
        self.entry2 = Entry(self.root, width=40)
        self.entry2.grid(row=1, column=1, sticky=W)
        self.entry2.bind('<KeyPress-Return>', self.bindEnter1)

        button = Button(self.root, text='开启服务', width=15, command=self.openChatWindow)
        # button = Button(self.root, text='开启服务', width=15, command=lambda: self.openChatWindow(entry1.get(), entry2.get()))
        button.grid(row=2, column=1, sticky=E, pady=5)

    # 新建一个聊天窗口
    def openChatWindow(self):
        if self.validateNotEmpty1() == True:
            self.toplevel = Toplevel(self.root)
            self.toplevel.title('服务端聊天窗口')
            x = int((self.width - 800) / 2)  # x轴偏移量
            y = int((self.height - 600) / 2)  # x轴偏移量
            self.toplevel.geometry('800x600+%s+%s' % (x, y))

            label1 = Label(self.toplevel, text='聊天室', background='red', fg='black', font=('微软雅黑', 12))
            label1.place(x=int((800 - label1.winfo_reqwidth()) / 2), y=10)

            self.msgText = Text(self.toplevel, width=85, height=18, fg='black', font=('微软雅黑', 12))
            self.msgText.place(x=5, y=50)
            scroll = Scrollbar(self.toplevel, command=self.msgText.yview)
            scroll.place(x=774, y=50, width=20, height=380)
            self.msgText.configure(yscrollcommand=scroll.set)
            self.msgText.tag_config('server', foreground='red')
            # self.msgText.tag_config('font1', font=('微软雅黑', 12))
            self.msgText.tag_config('newUser', foreground='green')
            self.msgText.tag_config('client', foreground='blue')

            label2 = Label(self.toplevel, text='发送消息', background='red', fg='black', font=('微软雅黑', 12))
            label2.place(x=5, y=440)
            self.inputText = Text(self.toplevel, width=87, height=4, fg='black', font=('微软雅黑', 12))
            self.inputText.place(x=5, y=470)
            self.inputText.bind('<KeyPress-Return>', self.bindEnter2)

            btnClear = Button(self.toplevel, width=10, anchor=CENTER, text='清屏', activeforeground='red',
                              activebackground='yellow', command=self.clearScreen)
            btnClear.place(relx=0.2, y=566)
            btnSend = Button(self.toplevel, width=10, anchor=CENTER, text='发送', activeforeground='red',
                             activebackground='yellow', command=self.sendMsg)
            btnSend.place(relx=0.7, y=566)

            self.toplevel.protocol('WM_DELETE_WINDOW', self.killThread)  # 自定义关闭窗口函数

            self.thread = threading.Thread(target=self.openSocket)
            self.thread.setDaemon(True)  # 确保主线程结束时,杀死子线程
            self.thread.start()

    # 开启Socket服务
    def openSocket(self):
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 获取本地主机名（可自定义）
            host = self.host
            # 设置端口号
            port = int(self.port)
            # 绑定主机和端口
            self.serverSocket.bind((host, port))
            # 设置最大连接数，超过后排队
            self.serverSocket.listen(5)
            # 接受客户端的请求则建立一个连接

            message = '当前主机：%s\n端口号：%s\n等待连接...\n' % (host, port)
            print(message)
            self.msgText.insert(END, message)
            # 禁用text控件以防止编辑修改
            self.msgText.config(state='disabled')

            self.connectionSocket, self.addr = self.serverSocket.accept()
            message = '有新的客人来啦！他的地址是：%s' % str(self.addr)
            print(message)
            self.msgText.config(state='normal')
            self.msgText.insert(END, message + '\n', 'newUser')
            self.connectionSocket.send(message.encode('utf8'))
            self.msgText.config(state='disabled')

            self.thread2 = threading.Thread(target=self.listenMsg)
            self.thread2.setDaemon(True)  # 确保主线程结束时,杀死子线程
            self.thread2.start()
        except Exception as e:
            print('打开Socket服务失败，请检查host和port！Error：%s' % e)

    # 监听客户端发送的消息
    def listenMsg(self):
        while True:
            try:
                # 监听客户端发送的消息并接收
                recvMsg = self.connectionSocket.recv(1024).decode('utf8')  # 注意是先监听到消息再获取的时间
                # recvTime = '客户端：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
                self.msgText.config(state='normal')
                # self.msgText.insert(END, recvTime + '\n', 'client')
                self.msgText.insert(END, recvMsg + '\n')
            except Exception as e:
                print('连接中断，Error：%s' % e)
                break
            finally:
                # 显示最新消息
                self.msgText.see(END)
                # 通过设置state属性设置textEdit不可编辑
                self.msgText.config(state='disabled')
                time.sleep(0.1)

    # 关闭聊天窗口结束子进程
    def killThread(self):
        try:
            msg = '逸轩（主机）退出啦！'
            self.connectionSocket.send(msg.encode('utf8'))
            # stop_thread(self.thread2)  # 关闭子线程
        except Exception as e:
            print('无客户端连接！Error：%s' % e)
        finally:
            self.serverSocket.close()  # 关闭Socket对象
            self.toplevel.destroy()  # 关闭（销毁）子窗口



    # host,port验证
    def validateNotEmpty1(self):
        if self.entry1.get() == '' or self.entry2.get() == '':
            messagebox.showinfo(title='Error', message='Host and Port can\'t not be null!')
            return False
        else:
            try:
                self.host = str(self.entry1.get())
                self.port = int(self.entry2.get())
                return True
            except ValueError:
                messagebox.showinfo(title='Error', message='请输入格式正确的host和port!')
                return False

    # 把按钮绑定给回车
    def bindEnter1(self, event):
        if event.keysym == 'Return':
            self.openChatWindow()   # 打开聊天窗口

    def bindEnter2(self, event):
        if event.keysym == 'Return':
            self.sendMsg()  # 发送消息

    # 清屏
    def clearScreen(self):
        self.msgText.config(state='normal')
        self.msgText.delete('0.0', END)
        self.msgText.config(state='disabled')
        # self.inputText.delete('0.0', END)

    # 发送消息
    def sendMsg(self):
        msg = self.inputText.get('0.0', END).strip()
        if msg == '':
            messagebox.showinfo(title='Error', message='发送消息不能为空或空格!')
        else:
            self.msgText.config(state='normal')
            sendTime = '主机（逸轩）:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            try:
                self.connectionSocket.send(sendTime.encode('utf8'))  # 服务端发送数据到客户端
                self.connectionSocket.send(msg.encode('utf8'))  # 没有客户端连接进来时，该方法会报错（因为连接对象未建立）...
                self.msgText.insert(END, sendTime + '\n', 'server')
                self.msgText.insert(END, msg + '\n')
            except Exception as e:
                self.msgText.insert(END, sendTime + '\n', 'server')
                msg += '（当前还没有客户端连接进来，服务端发送的消息只有自己看得到）'
                self.msgText.insert(END, msg + '\n')
                print('当前还没有客户端连接进来，服务端发送的消息只有自己看得到,Error:%s' % e)
            finally:
                # 显示最新消息
                self.msgText.see(END)
                # 消息框不可用
                self.msgText.config(state='disabled')
                # 清空输入框内容
                self.inputText.delete('0.0', END)


if __name__ == '__main__':
    # 实例化Server类
    Server()
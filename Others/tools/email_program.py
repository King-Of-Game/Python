# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# __date__ : 2019/10/3 23:10
# __software__ : PyCharm
# @Software: PyCharm

from email.header import decode_header
from email.parser import Parser
import poplib

import win32api
import win32con
import os
import time


VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0,
    'win':0x5B,
    'mouse_right':0x5D,
}

class Email:
    def __init__(self):
        '''设置邮箱的域名，端口，发送者邮箱，接收者邮箱'''
        self.toAddr = "test@163.com"

        '''设置收信的端口，密码'''
        self.pop3Host = "pop.163.com"
        self.receivePwd = "test"
        self.number = 0



    '''解析邮件主题'''
    def parser_subject(self, msg):
        subject = msg['Subject']
        value, charset = decode_header(subject)[0]
        if charset:
            value = value.decode(charset)
        return value
        # print('邮件主题： {0}'.format(value))





    '''收取邮件'''
    def receiveEmail(self):
        server = poplib.POP3(self.pop3Host)
        server.set_debuglevel(1)  # 设置打开或关闭调试信息
        # print(server.getwelcome().decode('utf-8'))  # 显示POP3服务器欢迎文字

        '''身份认证'''
        server.user(self.toAddr)
        server.pass_(self.receivePwd)


        # print(server.list())  # 返回：服务器响应；消息列表；返回消息大小
        emailList = server.list()[1]  # 得到所有邮件对象并返回一个列表
        # print(emailList)
        newIndex = len(emailList)   # 返回最新邮件的索引（这里邮件索引从1开始排列）
        self.number = newIndex

        # print(server.retr(newIndex))  # 返回：服务器响应；原始邮件内容；邮件所占字节
        lines = server.retr(newIndex)[1]  # 获取最新邮件的数据并返回一个列表
        msgContent = b'\r\n'.join(lines).decode('utf-8')  # 用换行符拼接列表成字符串并解码
        msg = Parser().parsestr(msgContent)  # 得到一个邮件对象

        subject = self.parser_subject(msg)  # 得到邮件标题
        server.quit()   # 关闭与服务器的连接，释放资源
        return subject





# 网易云暂停
def stopMusic():
    win32api.keybd_event(VK_CODE["ctrl"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["p"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["p"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

# 网易云上一首
def lastMusic():
    win32api.keybd_event(VK_CODE["ctrl"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["left_arrow"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["left_arrow"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

# 网易云下一首
def nextMusic():
    win32api.keybd_event(VK_CODE["ctrl"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, 0, 0)
    win32api.keybd_event(VK_CODE["right_arrow"], 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_CODE["right_arrow"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["alt"], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE["ctrl"], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

# 打开网易云
def openMusic():
    os.popen("D:\\CloudMusic\\cloudmusic.exe")  # 如果用os.system方法 必须等该进程执行完后
    time.sleep(2)


class Control:
    def __init__(self):
        self.num = 0

    def control(self):
        while True:
            # print(self.num)
            email = Email()
            result = email.receiveEmail()
            print("当前邮件总数为：%s" % email.number)


            if self.num != email.number:
                self.num = email.number
                if result == "暂停" or result == "播放":
                    stopMusic()
                    continue
                elif result == "上一首":
                    print(result)
                    lastMusic()
                    continue
                elif result == "下一首":
                    print(result)
                    nextMusic()
                    continue
                elif result == "网易云":
                    print(result)
                    openMusic()
                    continue
                elif result == "结束":
                    print(result)
                    break
                else:
                    print("未知命令")
                    continue

            else:
                time.sleep(3)
                continue










if __name__ == '__main__':
    control1 = Control()
    control1.control()




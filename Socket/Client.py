# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 7/28/2020 10:34 PM
# __software__ : PyCharm

import socket

# 创建socket对象
s = socket.socket()
# 目标本机主机名
host = 'msi'
# 设置目标端口号
port = 666

# 连接目标主机
s.connect((host, port))
s.send(('1').encode())

print(s.recv(1024).decode())    # 1024 是指定要接受的最大数据量

s.close()

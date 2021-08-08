# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 7/28/2020 9:41 PM
# __software__ : PyCharm


import socket

# 创建套接字对象
s = socket.socket()
# 获取本地主机名（可自定义）
host = socket.gethostname()
# host = 'msi'

# 设置端口号
port = 666
# 绑定主机和端口
s.bind((host, port))

print('当前主机：%s\n端口号：%s\n等待连接...' % (host, port))

# 等待客户端连接
s.listen(5)
while True:
    c, addr = s.accept()
    print('客户端连接地址：%s' % str(addr))
    data = '欢迎访问逸轩'
    # 向客户端发送消息
    c.send(data.encode())
    # 关闭连接
    c.close()


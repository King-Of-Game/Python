# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# __date__ : 2019/10/3 22:24
# __software__ : PyCharm
# @Software: PyCharm

from email.header import Header, decode_header
from email.utils import parseaddr
from email.mime.text import MIMEText
from email.parser import Parser
import base64
import smtplib
import poplib


class Email:
    def __init__(self):
        '''设置邮箱的域名，端口，发送者邮箱，接收者邮箱'''
        self.smtpHost = "smtp.qq.com"
        self.port = '465'
        self.fromAddr = "871437338@qq.com"
        self.password = "mpmcjenopidibefc"
        self.toAddr = "yixuanker@163.com"

        '''设置收信的端口，密码'''
        self.pop3Host = "pop.163.com"
        self.receivePwd = "zx454049162"

        '''构建文本邮箱的主体'''
        self.body = "这是测试内容"
        self.subject = "邮件标题"

    '''发邮件'''
    def sendEmail(self):
        msg = MIMEText(self.body, 'plain', 'utf-8')  # plain表示邮件内容的类型，文本类型默认是plain。utf-8表示内容的编码格式。
        msg['Subject'] = Header(self.subject, 'utf-8').encode()  # 收件方看到的邮件标题
        msg['From'] = 'YiXuan<%s>' % self.fromAddr               # 收件方看到的发件人
        msg['To'] = self.toAddr                                  # 收件方看到的收件人
        '''方法一'''
        server = smtplib.SMTP_SSL(self.smtpHost, 465)  # 加密SMTP
        server.login(self.fromAddr, self.password)
        server.sendmail(self.fromAddr, self.toAddr, msg.as_string())
        server.quit()

        '''方法二'''
        # server = smtplib.SMTP(self.smtpHost, 25)
        # server.login(self.fromAddr, self.password)
        # server.sendmail(self.fromAddr, self.toAddr, msg.as_string())
        # server.quit()

        '''方法三'''
        # server = smtplib.SMTP(self.smtpHost, 587)  # 加密SMTP
        # server.starttls()
        # server.login(self.fromAddr, self.password)
        # server.sendmail(self.fromAddr, self.toAddr, msg.as_string())
        # server.quit()


    '''解析邮件主题'''
    def parser_subject(self, msg):
        subject = msg['Subject']
        value, charset = decode_header(subject)[0]
        if charset:
            value = value.decode(charset)
        return value
        # print('邮件主题： {0}'.format(value))


    ''' 解析邮件来源'''
    def parser_address(msg):
        hdr, addr = parseaddr(msg['From'])
        # name 发送人邮箱名称， addr 发送人邮箱地址
        name, charset = decode_header(hdr)[0]
        if charset:
            name = name.decode(charset)
        print('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))


    '''解析邮件内容'''
    def parser_content(self, msg):
        content = msg.get_payload()

        # 文本信息
        content_charset = content[0].get_content_charset()  # 获取编码格式
        text = content[0].as_string().split('base64')[-1]
        text_content = base64.b64decode(text).decode(content_charset)  # base64解码

        # 添加了HTML代码的信息
        content_charset = content[1].get_content_charset()
        text = content[1].as_string().split('base64')[-1]
        html_content = base64.b64decode(text).decode(content_charset)

        print('文本信息: {0}\n添加了HTML代码的信息: {1}'.format(text_content, html_content))



    '''收取邮件'''
    def receiveEmail(self):
        server = poplib.POP3(self.pop3Host)
        server.set_debuglevel(1)  # 设置打开或关闭调试信息
        # print(server.getwelcome().decode('utf-8'))  # 显示POP3服务器欢迎文字

        '''身份认证'''
        server.user(self.toAddr)
        server.pass_(self.receivePwd)

        # print('Messages：%s. Size：%s' % server.stat())  # 返回邮件数量和占用空间（类型为元组）

        # print(server.list())  # 返回：服务器响应；消息列表；返回消息大小
        emailList = server.list()[1]  # 得到所有邮件对象并返回一个列表
        # print(emailList)
        newIndex = len(emailList)   # 返回最新邮件的索引（这里邮件索引从1开始排列）

        # print(server.retr(newIndex))  # 返回：服务器响应；原始邮件内容；邮件所占字节
        lines = server.retr(newIndex)[1]  # 获取最新邮件的数据并返回一个列表
        msgContent = b'\r\n'.join(lines).decode('utf-8')  # 用换行符拼接列表成字符串并解码
        msg = Parser().parsestr(msgContent)  # 得到一个邮件对象

        subject = self.parser_subject(msg)  # 得到邮件标题
        server.quit()   # 关闭与服务器的连接，释放资源
        return subject




if __name__ == '__main__':
    email = Email()
    # email.sendEmail()
    subject = email.receiveEmail()
    print(subject)





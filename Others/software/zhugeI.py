#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import requests
import lxml.html


def prediction():

    content = Text1.get('0.0', END)  # 获取Text1文本框的值
    content = content.strip()  # .strip()就是把这个字符串头和尾的空格去掉

    if content == "" or len(content) != 3:
        messagebox.showinfo('提示', '请输入三个汉字')
        Text1.delete(0.0, END)
    else:

        url = 'https://zhuge.911cha.com/'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'Referer': 'https://zhuge.911cha.com/'
        }
        data = {
            'q': content
        }
        request = requests.post(url=url, data=data, headers=header)
        data = request.text
        # print(data)  # 打印网页的内容
        select = lxml.html.document_fromstring(data)
        qianwen = select.xpath('//div[@class="mcon f14 l200"]/p/text()')
        jieqian = select.xpath('//div[@class="mcon f14 l200"]/p[4]/text()')



        Text2.delete(0.0, END)
        Text2.insert(INSERT, "%s：%s" % (qianwen[2], qianwen[3]))
        Text3.delete(0.0, END)
        Text3.insert(INSERT, jieqian[0][18:])





# 绘制窗体
root = Tk()
root.title("诸葛测字")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
w = int((width-462)/2)
h = int((height-230)/2)
root.geometry('462x230+%s+%s' % (w, h))

label1 = Label(root, text='请输入三个汉字：', fg='black')
label1.grid(row=0, column=0, sticky=E)
Text1 = Text(root, width=22, height=1, font=('微软雅黑', 10))
Text1.grid(row=0, column=1, sticky=W)
label2 = Label(root, text='签文：')
label2.grid(row=1, column=0, sticky=E)
Text2 = Text(root, width=44,height=3, font=('微软雅黑', 10))
Text2.grid(row=1, column=1, sticky=W)
label3 = Label(root, text='解签：')
label3.grid(row=2, column=0, sticky=E)
Text3 = Text(root, width=44,height=6, font=('微软雅黑', 10))
Text3.grid(row=2, column=1, sticky=W)
button1 = Button(root, text='测字', width=8, command=prediction)
button1.grid(row=3, column=0, sticky=W)
button2 = Button(root, text='退出', width=8, command=root.quit)
button2.grid(row=3, column=1, sticky=E)






# 消息循环
root.mainloop()







#!/usr/bin/python
# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/12/20
from tkinter import *
from tkinter import messagebox
import requests

def translate():

    content = Text1.get('0.0', END)
    # str.strip()就是把这个字符串头和尾的空格去掉
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '请输入需要翻译的内容')
    else:
        print(content)
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
        }
        data = {
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action:': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }
        request = requests.post(url, data, headers=header)
        print(request)
        json = request.json()
        print(json)
        temp = json['translateResult'][0][0]['tgt']
        Text2.delete(0.0, END)
        Text2.insert(INSERT, temp)


# 绘制窗体
root = Tk()
root.title("翻译工具")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
w = int((width-448)/2)
h = int((height-210)/2)
root.geometry('448x210+%s+%s' % (w, h))

label1 = Label(root, text='请输入需要翻译的文字：', fg='black')
label1.grid(row=0, column=0, sticky=E)
Text1 = Text(root, width=38, height=4, font=('微软雅黑', 10))
Text1.grid(row=0, column=1, sticky=W)
label2 = Label(root, text='翻译结果：')
label2.grid(row=1, column=0, sticky=E)
Text2 = Text(root, width=38,height=5, font=('微软雅黑', 10))
Text2.grid(row=1, column=1, sticky=W)
button1 = Button(root, text='翻译', width=8, command=translate)
button1.grid(row=2, column=0, sticky=W)
button2 = Button(root, text='退出', width=8, command=root.quit)
button2.grid(row=2, column=1, sticky=E)


# 消息循环
root.mainloop()







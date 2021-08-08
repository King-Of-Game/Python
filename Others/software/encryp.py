#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import base64  # Base64编码是从二进制到字符的过程
from Crypto.Cipher import AES


# 得到加/解密的内容并进行非空验证
def content():
    msg = Text1.get('0.0', END)
    # str.strip()就是把这个字符串头和尾的空格去掉
    msg = msg.strip()
    if msg == "":
        messagebox.showinfo('提示', '请输入需要加/解密的内容')
    else:
        return str(msg)

def jia():
    msg = entry1.get()
    msg = msg.strip()
    if msg == "":
        messagebox.showinfo('提示', '请输入加密密钥')
    else:
        return msg

def jie():
    msg = entry2.get()
    msg = msg.strip()
    if msg == "":
        messagebox.showinfo('提示', '请输入解密密钥')
    else:
        return msg


# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value.encode()) % 16 != 0:
        value += '\0'
    return value.encode('utf-8')


def jiami():
    Text2.delete(0.0, END)  # 每次清理文本框
    key = jia()  # 设置密钥16位
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加/解密器(把自己设置的密码输入到加/解密器)
    text = content()  # 需要加密的文本
    encrypt_aes = aes.encrypt(add_to_16(text))   # 进行AES加密
    base = base64.b16encode(encrypt_aes)   # 进行base64编码
    encrypted_text = base.decode('utf-8')  # 得到加密后的文本
    Text2.insert(INSERT, encrypted_text)  # 把加密的文本输出到文本框上


def jiemi():
    Text2.delete(0.0, END)  # 每次清理文本框
    key = jie()  # 设置密钥
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加/解密器(把自己设置的密码输入到加/解密器)
    encrypted_text = content()  # 得到加密后的文本
    base = base64.b16decode(encrypted_text.encode('utf-8'))  # 进行base64编码
    decryption_text = aes.decrypt(base).decode('utf-8').replace('\0', '')  # 解密
    Text2.insert(INSERT, decryption_text)  # 把解密后的文本输出到文本框上




# 绘制窗体
root = Tk()
root.title("AES工具")
width = root.winfo_screenwidth()  # 获取电脑窗体的宽度
height = root.winfo_screenheight() # 获取电脑窗体的高度
w = int((width-450)/2)
h = int((height-405)/2)
root.geometry('450x405+%s+%s' % (w, h))

label1 = Label(root, text='请输入需要加/解密的内容：')
label1.grid(row=0, columnspan=2, sticky=E+W)
Text1 = Text(root, width=74, height=9, font=('微软雅黑', 8))
Text1.grid(row=1, columnspan=2, sticky=E+W)



label2 = Label(root, text='请输入加密密钥：')
label2.grid(row=2, column=0, sticky=E+W)
entry1 = Entry(root, width=30, show='*')
entry1.grid(row=2, column=1, sticky=W)

Text2 = Text(root, width=74, height=9, font=('微软雅黑', 8))
Text2.grid(row=3, columnspan=2, sticky=E+W)

label3 = Label(root, text='请输入解密密钥：')
label3.grid(row=4, column=0, sticky=E+W)
entry2 = Entry(root, width=30, show='*')
entry2.grid(row=4, column=1, sticky=W)

button1 = Button(root, text='加密', width=7, height=1, font=('微软雅黑', 12), command=jiami)
button1.grid(row=5, column=0, sticky=W)
button3 = Button(root, text='解密', width=7, height=1, font=('微软雅黑', 12), command=jiemi)
button3.grid(row=5, column=1, sticky=E)


# 消息循环
root.mainloop()




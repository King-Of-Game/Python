#!/usr/bin/python
# -*- coding: utf-8 -*-
# 这里针对的是格式是.ts的视频文件。（这种格式的视频一般是经过VIP视频网站解析过得）
# 下面讲解思路：
# 1.首先打开浏览器比如谷歌：进入到视频播放页面，按F12然后进入Network下点击作色红色圆点右边的clear键清除加载的各种信息。
# 2.按下F5刷新界面，点击Network下的XHR分类标签，你会看到xxxx000.ts这种格式的文件。（F12调试工具请不要关闭）
# 3.把视频进度条拖到最后，你就会看到一个xxx999.ts，或者其他三位数的.ts文件，这就是最后一个.ts文件。（视频过长有可能是四位数）
# 4.把第一个.ts文件和最后一个.ts文件的Request URL进行对比，你就能找到规则。
# 5.用进程池，多进程爬取循环生成的url路径，在指定目录生成.ts文件
# 6.在Windows系统下的CMD命令行进入.ts文件目录下，用“copy /b *.ts abc.mp4”这个命令把所有.ts文件合并成一个.mp4文件（abc是命名，可以随意设置）
# 7.由于.ts文件是按照000、001这样的顺序排列的，所以正常情况下合并的mp4文件的播放的画面是正常且连续的。（不过也有意外情况，暂时没解决）


import requests
from multiprocessing import Pool

def temp(i):
    if i < 1000:
        url = "https://cdn1.chlpdq.com/20180906/2lQthu8i/800kb/hls/1P9Vmw92550%03d.ts" % i  # 三个0填充
    else:
        url = "https://cdn1.chlpdq.com/20180906/2lQthu8i/800kb/hls/1P9Vmw92550%04d.ts" % i

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers)
    print(url)
    # print(r.content) # .content 返回的是二进制数据 .text 返回的是字符串
    if i < 1000:
        with open('./mp4/{}'.format(url[-12:]), 'wb') as f:
            f.write(r.content)
    else:
        with open('./mp4/{}'.format(url[-13:]), 'wb') as f:
            f.write(r.content)





if __name__ == '__main__':
    pool = Pool(30)
    for i in range(2200):
        pool.apply_async(temp, (i,))# 创建一个进程
    pool.close()
    pool.join() # 加上这个就是让子进程结束，主进程才会结束。

# #D:\Python练习\mp4>copy /b *.ts abc.mp4


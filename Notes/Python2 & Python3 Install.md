# 同时安装 Py2 和 Py3

1. 官网下载并安装两个版本的Python
2. 配置环境变量
   1. python3: 在 path 添加 D:\py3.7 和 D:\py3.7\Scripts (前者表示python启动程序的环境变量，后者是pip的环境变量)
   2. python2: 在 path 添加 D:\py2.7 和 D:\py2.7\Scripts
3. 修改可执行文件的名字
   1. 修改python2中python.exe和pythonw.exe的名称为python2.exe、pythonw2.exe
   2. 修改python3中python.exe和pythonw.exe的名称为python3.exe、pythonw3.exe
4. pip 设置
   1. Python 安装包需要用到包管理工具pip，但是当同时安装python2和python3的时候，pip只是其中一个版本，以下将提供一个修改方式。
   2. 重新安装两个版本的pip，使得两个python版本的pip能够共存。
   3. python3 -m pip install --upgrade pip --force-reinstall
   4. python2 -m pip install --upgrade pip --force-reinstall
   5. 现在可以通过 pip2 -V 和 pip3-V 查看两个版本的pip信息，以后只需运行 pip2 install XXX 和 pip3  install XXX即可安装各自的python包。


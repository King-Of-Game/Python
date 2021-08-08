# pip 常用命令

## 更新 pip 

+  python -m pip install -U --force-reinstall pip

## 查找包

+ pip search Package

## 安装包

+ pip install Package
+ python3 -m pip install xxx -i http://mirrors.aliyun.com/pypi/simple/
+ pip install -r requirements.txt

## 安装 .whl 文件

+ pip install xxx.whl

## 更新包

+ pip install -U Package

## 卸载包

+ pip uninstall Package

## 列出已安装软件

+ pip list
+ pip freeze
+ pip freeze -r requirements.txt

## 将项目依赖的库重定向输出到文件

1. cd到项目根目录
2. pip projectname > requirements.txt

## 查看一个软件包时安装了哪些文件

+ pip show -f Package

## 命令补全

+ pip completion --bash >> .bash_profile

## 升级所有包

+ for i in `pip list --outdated --trusted-host pypi.douban.com | tail -n +3 | awk '{print $1}'`; do pip install -U $i; done

## 设置超时时间

+ pip --default-timeout=100 install -U Pillow
+ pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

## pip崩溃

+ 方案一：python -m ensurepip 然后执行 python -m pip install --upgrade pip 
+ 方案二：curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  python get-pip.py --force-reinstall

# 修改pip安装源

## mac 和 Linux

+ 需要自己创建.pip/目录和配置文件
+ mkdir ~/.pip
+ vim ~/.pip/pip.conf

## Windows

+ 在C:\Users\用户 目录下面，新建一个pip文件夹
+ 在pip文件夹下新建 pip.ini 文件
+ ![](C:\Users\Administrator\Desktop\Notebooks\Python\images\pip_win.png)

+ pip.ini文件的内容如下：

  + ```ini
    # 阿里源
    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple/
    trusted-host = mirrors.aliyun.com
    
    # 豆瓣源
    # [global]index-url = http://pypi.douban.com/simple
    # trusted-host = pypi.douban.com
    ```

  + 

 
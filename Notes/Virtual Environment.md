# Python 使用虚拟环境

1. 安装 virtualenvwrapper-win
   - pip install virtualenvwrapper-win
2. 添加环境变量
   1. 在系统变量里面点击新建
   2. 变量名：WORKON_HOME
   3. 变量值：存放虚拟环境的目录
3. 使设置生效
   - 双击pyhon\Scripts目录下的virtualenvwarpper.bat
4. 虚拟环境常用命令
   1. 创建虚拟环境
      - mkvirtualenv virtual1
   2. 使用/切换 某个虚拟环境
      - workon virtua
   3. 跳转到当前虚拟环境的目录
      - cdvirtualenv
   4. 离开虚拟环境
      - deactivate
   5. 删除当前虚拟环境
      - rmvirtualenv

# 直接用 python  创建虚拟环境

1. python -m venv [virul_name]   # 生成虚拟环境的目录
2. cd [virul_name]/Scripts/  # 进入虚拟环境的目录的Scripts目录下
3. activate  # 进入虚拟环境


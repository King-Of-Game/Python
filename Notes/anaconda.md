# 1. 安装

- 最后两个都勾选

# 2. 配置镜像源

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
conda config --set show_channel_urls yes
```

# 3. 常用命令

- conda info --envs  # 查看已安装的环境
- conda activate base  # 切换到默认环境
  - conda install packname / pip install packName  # 安装包
- conda create --name envName python=2.7  # 创建一个py27的开发环境
- conda remove --name envName --all  # 删除名为 envName 的环境


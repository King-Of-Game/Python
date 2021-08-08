FROM centos

MAINTAINER jack

RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
RUN curl -o /etc/yum.repos.d/CentOS-Base.repo https://raw.githubusercontent.com/hackyoMa/docker-centos/8/CentOS-Base.repo
RUN yum makecache
RUN yum -y install python36
RUN yum -y install gcc
RUN yum -y install python36-devel
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# 以上是构建python环境步骤，使用python镜像可省略
RUN mkdir /code

WORKDIR /code

COPY ../requirements.txt /code

RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=200 && \
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=200 && \
    rm requirements.txt

EXPOSE 8000


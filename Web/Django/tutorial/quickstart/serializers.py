#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/10/14 20:37
# __software__ : PyCharm

from django.contrib.auth.models import User
from .models import Article
from rest_framework import serializers


'''
验证器
'''
def check_length(value):
    length = len(value)
    if length < 2 or length > 6:
        raise serializers.ValidationError(f'标题字符长度为2~6')


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")

    class Meta:
        model = User
        fields = ('id', 'username', 'articles',)
        read_only_fields = ('id', 'username',)


class ArticleSerializer(serializers.ModelSerializer):
    # 如果希望author不可见并让DRF根据request.user自动补全这个字段
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    """改变序列化后的数据输出格式"""
    author = serializers.ReadOnlyField(source='author.username')
    # author = UserSerializer(read_only=True)  # required=False表示可接受匿名用户，many=True表示有多个用户。
    # status = serializers.ReadOnlyField(source='get_status_display')  # 把原来可读可修改的字段变成了只读
    # full_status = serializers.ReadOnlyField(source="get_status_display")  # 增加一个新的名为 “full_status” 的只读字段
    cn_status = serializers.SerializerMethodField()  # SerializerMethodField（自定义方法字段） 通常用于增加模型中原本不存在的字段（只读），不能通过反序列化对其直接进行修改
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)  # 格式化时间
    title = serializers.CharField(validators=[check_length])

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')

    def get_cn_status(self, obj):
        if obj.status == "p":
            return "已发表"
        elif obj.status == "d":
            return "草稿"
        else:
            return ""


#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/10/14 23:11
# __software__ : PyCharm

from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    re_path(r'^articles/$', views.ArticleList.as_view()),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(), name='article-detail'),
    re_path(r'^users/$', views.UserList.as_view()),
]

# 处理不同格式的url请求
urlpatterns = format_suffix_patterns(urlpatterns)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 12/4/2020 8:41 PM
# __software__ : PyCharm

from django.urls import path
from . import views


urlpatterns = [
    path('serial_list/page=<page_num>', views.serial_list, name='serial_list'),

    # 列表分页
    # path('show_serial_list/<page_num>', views.show_serial_list, name='show_serial_list'),

    # ajax接口
    path('search_item/', views.search_item),

]

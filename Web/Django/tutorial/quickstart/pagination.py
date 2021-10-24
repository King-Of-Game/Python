#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 2021/10/17 22:14
# __software__ : PyCharm

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3   # 设置默认每页显示数目
    page_size_query_param = 'size'  # 设置参数名称p
    max_page_size = 10  # 设置每页最大显示数目

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'code': 200,
            'results': data
        })

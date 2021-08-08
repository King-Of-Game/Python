# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 12/7/2019 11:16 PM
# __software__ : PyCharm

import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.contrib import auth

from django.urls import reverse
from django.db import connection  # 执行原生sql

from studentManage.models import User


# 返回登录界面
def login(request):

    return render(request, 'login.html')


# 检查登录
def checkLogin(request):
    content = {
        'status': 0  # 状态为0则登录失败
    }

    if request.method == "POST":
        account = request.POST['account']
        pwd = request.POST['pwd']
        if account == '' or pwd == '':
            content['msg'] = '账号或密码不能为空！'
        else:
            user_obj = User.objects.filter(account=account, password=pwd)
            # print(user)
            if len(user_obj) > 0:
                user_dict = user_obj.values()[0]
                print(user_dict)
                request.session['account'] = user_dict['account']
                request.session['nickname'] = user_dict['nickname']
                request.session['roleID'] = user_dict['roleID']
                print(request.session['account'])
                print(request.session['nickname'])
                print(request.session['roleID'])
                content['status'] = 1  # 登录成功
                content['msg'] = '登陆成功！'
            else:
                content['msg'] = '账号或密码错误！'
    return JsonResponse(content)








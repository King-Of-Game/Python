"""ScoreManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentManage, name='studentManage'),

    # iframe
    path('welcome/', views.welcome, name='welcome'),
    path('chooseSubject/', views.chooseSubject, name='chooseSubject'),
    path('scoreDetail/', views.scoreDetail, name='scoreDetail'),
    path('userDetail/', views.userDetail, name='userDetail'),
    path('addAccount/', views.addAccount, name='addAccount'),


    # ajax接口
    path('getSession/', views.getSession, name='getSession'),
    path('clearSession/', views.clearSession, name='clearSession'),
    path('getChooseSubject/', views.getChooseSubject, name='getChooseSubject'),
    path('confirmSubject/', views.confirmSubject, name='confirmSubject'),
    path('cancelSubject/', views.cancelSubject, name='cancelSubject'),
    path('getScoreByRole/', views.getScoreByRole, name='getScoreByRole'),
    path('updateScore/', views.updateScore, name='updateScore'),
    path('getUserByRole/', views.getUserByRole, name='getUserByRole'),
    path('updatePwd/', views.updatePwd, name='updatePwd'),
    path('resetPwd/', views.resetPwd, name='resetPwd'),
    path('addUser/', views.addUser, name='addUser'),

]

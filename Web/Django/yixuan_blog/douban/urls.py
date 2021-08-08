#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 12/4/2020 8:41 PM
# __software__ : PyCharm

from django.urls import path
from . import views


urlpatterns = [
    path('film_list/page=<page_num>', views.film_list, name='film_list'),
    path('emotion_analysis/film_id=<film_id>', views.emotion_analysis, name='emotion_analysis'),
    path('film_reviews/film_id=<film_id>/page=<page_num>', views.film_reviews, name='film_reviews'),

    # ajax接口
    path('search_item/', views.search_item, name='search_item'),
    path('edit_film/', views.edit_film, name='edit_film'),
    path('del_film/', views.del_film, name='del_film'),


]

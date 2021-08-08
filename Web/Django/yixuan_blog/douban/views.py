from django.shortcuts import render
from douban.models import FilmDetail
from douban.models import FilmReview
from django.core.paginator import Paginator
from django.db import connection
from django.http import JsonResponse
import datetime

# Create your views here.


# 首页电影信息分页显示
def film_list(request, page_num):

    film_lists = FilmDetail.objects.order_by('-film_rate')  # 按照日期倒叙排序
    # print(film_lists.values()[0])

    paginator = Paginator(film_lists, 15)  # 显示前15条数据

    page_num = 1 if page_num == "" else int(page_num)

    now_page = paginator.page(page_num)  # 返回第number页的page类实例对象

    page_list = []
    num_pages = paginator.num_pages  # 返回分页之后的总页数
    page_range = paginator.page_range  # 返回分页后的页码列表

    # 最多显示5个页码
    if num_pages >= 5:
        if 3 <= page_num <= num_pages - 2:
            page_list = page_range[page_num - 3:page_num + 2]
        elif page_num < 3:
            page_list = page_range[:page_num + 2]
        elif page_num > num_pages - 2:
            page_list = page_range[page_num-3:num_pages]
    else:
        page_list = page_range

    context = {
        "now_page": now_page,  # 当前页码包含有15条数据的 paginator 对象
        "page_list": page_list,  # 页码列表

    }

    return render(request, "douban/film_list.html", context)


# 模糊查询
def search_item(request):
    search_text = request.GET['search_text']
    film_details = FilmDetail.objects.filter(film_title__contains=search_text).values()
    # print(film_details)

    result = {
        'data': list(film_details)
    }
    return JsonResponse(result)


# 编辑电影信息
def edit_film(request):
    film_id = request.POST["film_id"]
    film_name = request.POST["film_name"]

    data = {}
    try:
        FilmDetail.objects.filter(film_id=film_id).update(film_title=film_name)
        data['status'] = 1  # 成功
    except:
        data['status'] = 0  # 失败

    return JsonResponse(data)


# 删除某条电影及它的相关评论数据
def del_film(request):
    film_id = request.POST['film_id']
    data = {}
    try:
        FilmDetail.objects.filter(film_id=film_id).delete()
        FilmReview.objects.filter(film_id=film_id).delete()
        data['status'] = 1  # 成功
    except:
        data['status'] = 0  # 失败

    return JsonResponse(data)


# 电影情感分析
def emotion_analysis(request, film_id):
    sql = "SELECT * \
        from douban_filmdetail \
        where film_id='%s';" % film_id
    cursor = connection.cursor()
    cursor.execute(sql)
    tup_items = cursor.fetchall()

    context = {}
    for tup in tup_items:
        json = {
            'film_id': tup[0],
            'film_title': tup[1],
            'film_rate': tup[2],
            'positive_emotion': tup[3],
            'negative_emotion': tup[4],
            'total_score': tup[5],
            'film_result': tup[6],
        }
        context = {
            "data": json
        }

    return render(request, "douban/pie_chart.html", context=context)


# 电影评论分页显示
def film_reviews(request, film_id, page_num):
    film_reviews_lists = FilmReview.objects.filter(film_id=film_id).order_by('-film_review_date').all()
    film_detail = FilmDetail.objects.get(film_id=film_id)

    paginator = Paginator(film_reviews_lists, 3)

    page_num = 1 if page_num == "" else int(page_num)

    now_page = paginator.page(page_num)  # 返回第number页的page类实例对象

    page_list = []
    num_pages = paginator.num_pages  # 返回分页之后的总页数
    page_range = paginator.page_range  # 返回分页后的页码列表

    if num_pages >= 5:
        if 3 <= page_num <= num_pages - 2:
            page_list = page_range[page_num - 3:page_num + 2]
        elif page_num < 3:
            page_list = page_range[0:page_num + 2]
        elif page_num > num_pages - 2:
            page_list = page_range[page_num-3:num_pages]
    else:
        page_list = page_range

    context = {
        "now_page": now_page,  # 当前页码：paginator对象
        "page_list": page_list,  # 页码列表
        "film_detail": film_detail  # 对应电影的信息
    }

    return render(request, "douban/film_reviews.html", context)

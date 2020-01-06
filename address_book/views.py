from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User
from index.views import logging_check


# Create your views here.
# @logging_check
def address_book_view(request):
    return render(request, "address_book/index_first.html")


def address_book_list(request):
    if request.method == "GET":
        all_user = User.objects.all()
        paginator = Paginator(all_user, 15)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "address_book/YuanGonglist.html", locals())
    elif request.method == "POST":
        # service = request.POST.get("department")
        # print(service)
        query = request.POST.get("query")
        users = User.objects.filter(username=query)
        paginator = Paginator(users, 15)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "address_book/YuanGonglist.html", locals())

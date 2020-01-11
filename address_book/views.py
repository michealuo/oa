from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from index.views import logging_check
from management.models import Management


@logging_check
def address_book_list(request):
    if request.method == "GET":
        all_user = Management.objects.all()
        paginator = Paginator(all_user, 10)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "address_book/YuanGonglist.html", locals())
    elif request.method == "POST":
        department = request.POST.get("department")
        query = request.POST.get("query")
        if not query and not department:
            return HttpResponseRedirect("/address_book/list")
        elif query and not department:
            users = Management.objects.filter(name=query)
            if not users:
                users = Management.objects.filter(phone=query)
        elif not query and department:
            users = Management.objects.filter(dep_name=department)
        else:
            users = Management.objects.filter(name=query, dep_name=department)
            if not users:
                users = Management.objects.filter(phone=query, dep_name=department)
        paginator = Paginator(users, 10)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "address_book/YuanGonglist.html", locals())


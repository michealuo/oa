from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User
from index.views import logging_check


# Create your views here.
@logging_check
def address_book_view(request):
    return render(request, "address_book/index_first.html")


def address_book_list(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "address_book/YuanGonglist.html", locals())
    elif request.method == "POST":
        service = request.POST.get("department")
        print(service)
        query = request.POST.get("query")
        users = User.objects.filter(username=query)
        return render(request, "address_book/YuanGonglist.html", locals())

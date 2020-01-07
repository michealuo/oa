from django.shortcuts import render
from user.models import User
from index.views import logging_check


# Create your views here.
@logging_check
def notice_list(request):
    return render(request, "notice/notice_list.html")


@logging_check
def notice_add_view(request):
    return render(request, "notice/notice_add.html")


@logging_check
def notice_view(request):
    return render(request, "notice/notice.html")

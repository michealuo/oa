from django.shortcuts import render
from user.models import User


# Create your views here.
def index_view(request):
    return render(request, "notice/index_first.html")


def notice(request):
    return render(request, "notice/GongGao.html")


def notice_add_view(request):
    return render(request, "notice/notice_add.html")


def notice_view(request):
    return render(request, "notice/GongGao1.html")

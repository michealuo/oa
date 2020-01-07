from django.shortcuts import render
from user.models import User


# Create your views here.
def notice_list(request):
    return render(request, "notice/notice_list.html")


def notice_add_view(request):
    return render(request, "notice/notice_add.html")


def notice_view(request):
    return render(request, "notice/notice.html")

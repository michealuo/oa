from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User


# Create your views here.
def address_book_view(request):
    return render(request, "communication/index_first.html")


def address_book_list(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "communication/YuanGonglist.html", locals())
    elif request.method == "POST":
        service = request.POST.get("department")
        query = request.POST.get("query")
        users = User.objects.filter(username=query)
        return render(request, "communication/YuanGonglist.html", locals())

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from report.models import Report_list


# Create your views here.


def first_index(request):
    return render(request, "report/index_first.html")


def list(request):
    uid = request.session.get("uid")
    lis = Report_list.objects.filter(user_id=uid)
    return render(request, "report/report_list.html",locals())


def add(request):
    if request.method == "GET":
        return render(request, "report/report_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if not content:
            return HttpResponse("----请输入内容----")
        if not title:
            return HttpResponse("----请输入标题----")


        Report_list.objects.create(title=title,content=content,user_id=request.session["uid"])

        return HttpResponseRedirect("/report/list")









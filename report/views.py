from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from report.models import Report_list


# Create your views here.


def list(request):
    uid = request.session.get("uid")
    lis = Report_list.objects.filter(user_id=uid).order_by("-updated_time")
    # print(lis[0].content[:5])
    return render(request, "report/report_list.html",locals())


def add(request):
    if request.method == "GET":
        return render(request, "report/report_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if not title or not content:
            return HttpResponseRedirect("/report/content")


        Report_list.objects.create(title=title,content=content,user_id=request.session["uid"])

        return HttpResponseRedirect("/report/list")


def content(request):
    return render(request,"report/content.html")


def update(request,id):
    report = Report_list.objects.get(id=id)
    if request.method == "GET":
        return render(request, "report/report_update.html",locals())
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if not title or not content:
            return HttpResponseRedirect("/report/content")

        is_update = False
        if report.title != title or report.content != content:
            is_update = True

        if is_update:
            report.title = title
            report.content = content
            report.save()

        return HttpResponseRedirect("/report/list")


def delete(request,id):
    report = Report_list.objects.get(id=id)
    try:
        report.delete()
    except Exception as e:
        print("删除失败")
        print(e)
        return HttpResponse("-------删除失败--------")
    return HttpResponseRedirect("/report/list")


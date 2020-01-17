import datetime
import re

from django.http import HttpResponse
from django.shortcuts import render
from management.models import Management
from .models import TimeBook
from index.views import *
# Create your views here.
@logging_check
def timebook_view(request):

    if request.method == 'GET':
        user_id1 = request.session.get('id1')
        user_id = request.session.get('uid')
        manage = Management.objects.get(id=user_id)
        power = manage.power
        print(power)
        if user_id1:
            user_id = user_id1
        manage = Management.objects.get(id=user_id)
        name = manage.name
        timebooks = TimeBook.objects.filter(management_id=user_id, ).order_by('-date')
        count = len(timebooks)
        return render(request, 'timebook/timebook_manage.html', locals())

    elif request.method == 'POST':
        date = request.POST.get('date')
        user_id1 = request.session.get('id1')
        user_id = request.session.get('uid')
        manage = Management.objects.get(id=user_id)
        power = manage.power
        print(power)
        if user_id1:
            user_id = user_id1
        manage = Management.objects.get(id=user_id)
        name = manage.name
        timebooks = TimeBook.objects.filter(management_id=user_id, date=date)
        count = len(timebooks)
        return render(request, 'timebook/timebook_manage.html', locals())



@logging_check
def month_view(request):

    if request.method == 'GET':
        date = request.POST.get('date')
        user_id1 = request.session.get('id1')
        user_id = request.session.get('uid')
        manage = Management.objects.get(id=user_id)
        power = manage.power
        print(power)
        if user_id1:
            user_id = user_id1
        manage = Management.objects.get(id=user_id)
        name = manage.name
        month = request.GET.get('month')
        if not month:
            return HttpResponse('请选择月份')
        print(month)
        timebooks = []
        timebooks_all= TimeBook.objects.filter(management_id=user_id).order_by('-date')
        if timebooks_all:
            for timebook in timebooks_all:
                print(timebook.date)
                if str(month) in str(timebook.date):
                    timebooks.append(timebook)

        else:
            timebooks=[]
        count = len(timebooks)
        return render(request, 'timebook/timebook_manage.html', locals())

@logging_check
def check_view(request):
    job_no = request.GET.get('job_no')
    print(job_no)
    try:
        manage = Management.objects.get(job_no=job_no)
        request.session['id1'] = manage.id
        print(manage.id)
        return HttpResponseRedirect('/timebook/list')
    except Exception as e:
        return HttpResponse('亲还未入职,请联系管理员')
    # timebooks = TimeBook.objects.filter(management_id=user_id, ).order_by('-date')
    # return render(request, 'timebook/timebook_manage.html', locals())
@logging_check
def update_view(request):
    if request.method == 'GET':
        statu_list = ['正常', '旷工', '请假', '迟到', '早退']
        management_id = request.GET.get('id')
        date1 = request.GET.get('date')
        res = re.findall(r'(\d*)年(\d*)月(\d*)日', date1)[0]
        date = datetime.date(int(res[0]), int(res[1]), int(res[2]))
        timebook = TimeBook.objects.get(date=date,management_id=management_id)
        manage = Management.objects.get(id=management_id)
        return render(request,'timebook/timebook_update.html',locals())
    elif request.method == 'POST':
        try:
            name = request.POST.get('name')
            manage = Management.objects.get(name=name)
        except Exception as e:
            return HttpResponse('该用户不存在')
        date1 = request.POST.get('date')
        res = re.findall(r'(\d*)年(\d*)月(\d*)日', date1)[0]
        date = datetime.date(int(res[0]), int(res[1]), int(res[2]))
        print(date,'1',date1)
        timebook = TimeBook.objects.filter(management_id=manage.id,date=date)
        present_statu = request.POST.get('present_statu')
        try:
            comment = request.POST.get('comment')
        except Exception as e:
            comment = ''
        print(name,date,comment,manage,present_statu)
        timebook.update(present_statu=present_statu,date=date)
        return HttpResponseRedirect('/timebook/list',locals())

@logging_check
def insert_view(request):
    statu_list = ['正常', '旷工', '请假', '迟到', '早退']
    if request.method == 'GET':
        id = request.session['id1']
        manage = Management.objects.get(id=id)
        name = manage.name
        return render(request, 'timebook/timebook_insert.html', locals())
    elif request.method == 'POST':
        user_id = request.session.get('id1')
        name = request.POST.get('name')
        try:
            manage = Management.objects.get(name=name)
            print(name,manage)
        except Exception as e:
            return HttpResponse('该用户不存在')

        date = request.POST.get('date')
        print(date)
        timebook = TimeBook.objects.filter(management_id=manage.id,date=date)
        if timebook:
            return HttpResponse('该天已登记')
        present_statu = request.POST.get('present_statu')
        if present_statu not in statu_list:
            return HttpResponse('请选择出勤状态')
        try:
            comment = request.POST.get('comment')
        except Exception as e:
            comment = ''
        timebook = TimeBook.objects.create(date=date,
                                           present_statu=present_statu,
                                           comment=comment,
                                           management_id=manage.id
                                           )
        return HttpResponseRedirect('/timebook/list')


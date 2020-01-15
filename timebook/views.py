
from django.shortcuts import render
from management.models import Management
from .models import TimeBook
from index.views import *
# Create your views here.
@logging_check
def timebook_view(request):
    user_id = request.session.get('uid')
    print(user_id)
    try:
        manager = Management.objects.get(user_id=user_id)
        name = manager.name
    except Exception as e:
        print(e)
        return HttpResponse('用户名不存在')

    if request.method == 'GET':

        timebooks = TimeBook.objects.filter(user_id=user_id, ).order_by('-date')
        manager = Management.objects.get(user_id=user_id)
        return render(request, 'timebook/time_book_manage.html', locals())

    elif request.method == 'POST':
        user_id = request.GET.get('id1')
        if not user_id:
            user_id = request.session.get('uid')
            date = request.POST.get('date')
            print(date)
            try:
                timebooks = TimeBook.objects.filter(user_id=user_id, date=date)
                print(timebooks)
                return render(request, 'timebook/time_book_manage.html', locals())
            except Exception as e:
                timebooks = []
                return render(request, 'timebook/time_book_manage.html', locals())



@logging_check
def month_view(request):
    user_id = request.GET.get('id1')
    if not user_id:
        user_id = request.session.get('uid')

    if request.method == 'GET':
        month = request.GET.get('month')
        list = []
        timebooks = TimeBook.objects.all()
        for timebook in timebooks:
            print(timebook.date)
            if month in timebook.date:
                list.append(timebook)
        timebooks = list

        return render(request, 'timebook/time_book_manage.html', locals())

@logging_check
def check_view(request):
    user_id = request.GET.get('id1')
    try:
        manager = Management.objects.get(user_id=user_id)
        name = manager.name
        request.session['id1'] = user_id
        request.session['uname'] = name
        print(manager)

    except Exception as e:
        print(e)
        return HttpResponse('用户不存在')
    timebooks = TimeBook.objects.filter(user_id=user_id, ).order_by('-date')
    return render(request, 'timebook/time_book_manage.html', locals())
def update_view(request):
    return HttpResponse('ok')

def insert_view(request):
    return render(request, 'timebook/timebook_insert.html', locals())
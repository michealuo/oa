import os
import socket

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
# 检查登录装饰器
from department.models import Position
from management.models import Management
from new_project import settings
from user.models import User, IpInfo
from notice.models import Notice_list


def logging_check(fn):
    def wrap(request, *args, **kwargs):
        #检查登录状态
        if not request.session.get('uid') or not request.session.get('username'):
            #没登录?
            if not request.COOKIES.get('uid') or not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else:
                #回写session
                uid = request.COOKIES.get('uid')
                username = request.COOKIES.get('username')
                request.session['uid'] = uid
                request.session['username'] = username


        uid = request.session['uid']
        #TODO 直接查询出用户数据 将用户对象绑定给request
        #user = User.obejcts.get(id=uid)
        #request.my_user = user

        request.my_uid = uid
        return fn(request,*args, **kwargs)
    return wrap


@logging_check
def index_views(request):
    username = request.session.get("username")
    management = Management.objects.get(username=username)
    notice_list = Notice_list.objects.all().order_by("-created_time")[:3]
    return render(request,'index/index.html', locals())


@logging_check
def index_first_view(request):

    return render(request,'index/index_first.html')

@logging_check
def index_view(request):
    username = request.session.get("username")
    management = Management.objects.get(username=username)
    return render(request,'index/index.html',locals())

@logging_check
def daily_mykh_view(request):

    return render(request,'index/daily_mykh.html')

@logging_check
def index_my_info(request):
    # user_info = Position.objects.all()
    uid = request.session.get("uid")
    username = request.session.get("username")
    user = User.objects.get(id=uid, username=username)

    # print(user_info)
    return render(request,'index/My_info.html',locals())

@logging_check
def index_my_ip(request):
    if request.method == "GET":
        all_user = IpInfo.objects.all()
        paginator = Paginator(all_user, 5)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "index/My_IP.html", locals())
    elif request.method == "POST":
        # service = request.POST.get("department")
        # print(service)
        query = request.POST.get("query")
        users = IpInfo.objects.filter(username=query)
        paginator = Paginator(users, 5)
        # 获取当前页码
        c_page = request.GET.get("page", 1)
        # 初始化当前页的page对象
        page = paginator.page(c_page)
        return render(request, "index/My_IP.html", locals())

@logging_check
def index_my_bj(request):
    if request.method == 'GET':
        return render(request, 'index/My_BJ.html')
    if request.method == 'POST':
        # 处理数据
        file = request.FILES['myfile']
        filename = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(filename, 'wb') as f:
            data = file.file.read()
            f.write(data)

    return render(request,'index/My_BJ.html',locals())

@logging_check
def index_my_mim(request):
    if request.method == 'GET':
        uid = request.session.get("uid")
        username = request.session.get("username")
        user = User.objects.get(id=uid, username=username)
        return render(request,'index/My_mim.html',locals())
    elif request.method == 'POST':
        uid = request.session.get("uid")
        username = request.session.get("username")
        old_pwd = request.POST.get('old_pwd')
        # hash 加密
        import hashlib
        m = hashlib.md5()
        m.update(old_pwd.encode())
        user = User.objects.get(id=uid, username=username)
        if user.password != m.hexdigest():
            msg = '原密码不正确'
        else:
            msg = '密码修改成功'
            new_pwd_1 = request.POST.get('new_pwd_1')
            new_pwd_2 = request.POST.get('new_pwd_2')
            if new_pwd_1 != new_pwd_2:
                msg = '两次密码不一样'
                return render(request,'index/My_mim.html',locals())
            if old_pwd == new_pwd_1:
                msg = '原密码和新密码一致'
                return render(request,'index/My_mim.html',locals())
            m = hashlib.md5()
            m.update(new_pwd_1.encode())
            user.password = m.hexdigest()
            user.save()
        return render(request,'index/My_mim.html',locals())



def child_view(request,app,info):
    return render(request,'index/child.html',locals())

def child_notice_view(request,app,info,id):
    return render(request,'index/child.html',locals())



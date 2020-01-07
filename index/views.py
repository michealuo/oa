import socket

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
# 检查登录装饰器
from user.models import User, IpInfo


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
    return render(request,'index/index.html')


@logging_check
def index_first_view(request):

    return render(request,'index/index_first.html')

@logging_check
def index_view(request):

    return render(request,'index/index.html')

@logging_check
def daily_mykh_view(request):

    return render(request,'index/daily_mykh.html')

@logging_check
def index_my_info(request):
    uid = request.session.get("uid")
    username = request.session.get("username")
    user = User.objects.get(id=uid, username=username)
    return render(request,'index/My_info.html',locals())

@logging_check
def index_my_ip(request):
        user_ip_info = IpInfo.objects.all()
        print(user_ip_info)
        return render(request,'index/My_IP.html',locals())

@logging_check
def index_my_bj(request):
    return render(request,'index/My_BJ.html')

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



def child_view(request,app,info):

    return render(request,'index/child.html',locals())



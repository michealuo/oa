from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 检查登录装饰器
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

    return render(request,'index/My_info.html')

@logging_check
def index_my_ip(request):

    return render(request,'index/My_IP.html')

@logging_check
def index_my_bj(request):

    return render(request,'index/My_BJ.html')

@logging_check
def index_my_mim(request):

    return render(request,'index/My_mim.html')

@logging_check
def myfirst_view(request):

    return render(request,'index/Myfirst.html')
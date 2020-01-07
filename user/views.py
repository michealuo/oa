from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from user.models import User

def reg_view(request):

    if request.method == 'GET':
        #获取页面
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #处理注册请求
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(email)
        #判断username是否已经被注册
        users = User.objects.filter(username=username)
        if users:
            #用户名已注册
            return HttpResponse('用户名已经被注册!')

        if password_1 != password_2:
            #两次密码不一致
            return HttpResponse('两次密码不一致')

        #hash md5 加密明文密码
        import hashlib
        m = hashlib.md5()
        m.update(password_1.encode())

        try:
            user = User.objects.create(username=username,password = m.hexdigest(),phone=phone,email=email)
        except Exception as e:

            print('---注册错误---')
            print(e)
            return HttpResponse('--Serve is Busy')

        #注册成功
        resp =  HttpResponseRedirect('/user/login')
        resp.set_cookie('username', username, 3600*24)
        resp.set_cookie('uid', user.id, 3600*24)
        return resp


def login_view(request):
    # 登录处理
    if request.method == 'GET':
        # 1,优先检查session
        if request.session.get('uid') and request.session.get('username'):
            # 登陆过
            return HttpResponseRedirect('/index/index')
        # 2,检查cookies
        uid = request.COOKIES.get('uid')
        username = request.COOKIES.get('username')
        if uid and username:
            # 回写session
            request.session['uid'] = uid
            request.session['username'] = username
            return HttpResponseRedirect('/index/index')
        return render(request, 'user/login.html')

    elif request.method == 'POST':

        # 处理数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        old_users = User.objects.filter(username=username)
        if not old_users:
            return HttpResponse('---Username or password is wrong')
        # 校验密码
        import hashlib
        m = hashlib.md5()
        m.update(password.encode())

        user = old_users[0]
        if user.password != m.hexdigest():
            # 密码错误
            return HttpResponse('Username or password is wrong~')
        # 保存登录状态
        # 1， 存session
        request.session['uid'] = user.id
        request.session['username'] = username
        resp = HttpResponseRedirect('/index/index')
        # if 'isSaved' in request.POST.keys():
        #     # 用户勾选了 下次免登陆
        #     resp.set_cookie('uid', user.id, 3600 * 24 * 30)
        #     resp.set_cookie('username', username, 3600 * 24 * 30)
        return resp




def logout(request):
    # 登出
    # 删除 session

    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']
    # 删除 Cookies
    resp = HttpResponseRedirect('login')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp


def forget(request):
    return render(request,'/user/forget.html')


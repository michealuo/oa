import json
import random
import socket

from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from pymysql import DatabaseError

from management.models import Management
from user.models import User, IpInfo


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
        #判断username是否已经被注册
        users = User.objects.filter(username=username)
        if users:
            #用户名已注册
            msg = '用户名已注册'
            return render(request,'user/register.html',locals())

        if password_1 != password_2:
            #两次密码不一致
            msg = '两次密码不一致'
            return render(request,'user/register.html',locals())

        #hash md5 加密明文密码
        import hashlib
        m = hashlib.md5()
        m.update(password_1.encode())
        #作为一个事务
        try:
            with transaction.atomic():
                try:
                    user = User.objects.create(username=username,password = m.hexdigest(),phone=phone,email=email)
                    management = Management.objects.create(username=username,phone=phone,email=email,user=user)
                except Exception as e:
                    print('---注册错误---')
                    print(e)
                    msg = '注册错误'
                    raise DatabaseError

        except DatabaseError:
            return render(request, 'user/register.html', locals())

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
            # 存ip
            save_host_ip(username)
            return HttpResponseRedirect('/index/index')

        return render(request, 'user/login.html')

    elif request.method == 'POST':
        # 处理数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        old_users = User.objects.filter(username=username)
        if not old_users:
            msg = '用户名或者密码错误'
            return render(request,'user/login.html',locals())
        # 校验密码
        import hashlib
        m = hashlib.md5()
        m.update(password.encode())
        user = old_users[0]
        if user.password != m.hexdigest():
            # 密码错误
            msg = '密码错误'
            return render(request,'user/login.html',locals())
        # 保存登录状态
        # 1， 存session
        request.session['uid'] = user.id
        request.session['username'] = username
        resp = HttpResponseRedirect('/index/index')
        # 存ip
        save_host_ip(username)
        # ip_info = IpInfo.objects.filter(ip_adress=)
        # if save_host_ip(username) == ip_info.ip_adress:


        return resp

def save_host_ip(uname):
    """
    查询本机ip地址
    :return: ip
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    user_ip_info = IpInfo.objects.create(uname = uname,ip_adress=ip)
    IpInfo.save(user_ip_info)

def update_info(request):
    users = User.objects.filter(id=id, isActive=True)
    if not users:
        return HttpResponse('--The user id is wrong !')
    book = users[0]

    if request.method == 'GET':
        # 拿更新页面
        return render(request, 'index/MY_IP.html', locals())
    elif request.method == 'POST':
        # 更新数据
        username = request.POST.get('username')
        if not username:
            return HttpResponse('---Please give me price')
        phonenumber = request.POST.get('phonenumber')
        # TODO 检查market_price

        # 是否要更新?
        to_update = False
        if username != str(users.username):
            to_update = True

        if phonenumber != str(users.phonenumber):
            to_update = True

        if to_update:
            # 执行更新
            print('--执行更新')
            users.username = username
            users.phonenumber = phonenumber
            users.save()

        # 更新完毕后 执行302跳转 跳转回 book首页 - all_book
        # 302参数 是 url!!!!!!!!!!
        return HttpResponseRedirect('/index/my_ip')

def logout(request):
    # 登出
    # 删除 session
    if 'uid' in request.session:
        del request.session['uid']
    if 'username' in request.session:
        del request.session['username']
    if 'id1' in request.session:
        del request.session['id1']
    # 删除 Cookies
    resp = HttpResponseRedirect('login')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp



def findpwd(request):
    global number
    if request.method == 'GET':
        # 获取页面
        return render(request, 'user/findpwd.html')
    elif request.method == 'POST':
        # 处理注册请求
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        code = request.POST.get('code')
        # 判断username是否已经被注册
        users = User.objects.get(username=username)
        if int(code) != number:
            msg = '验证码错误'
            return render(request, 'user/findpwd.html', locals())


        if not users:
            # 用户名已注册
            msg = '用户名错误'
            return render(request, 'user/findpwd.html', locals())

        if password_1 != password_2:
            # 两次密码不一致
            msg = '两次密码不一致'
            return render(request, 'user/findpwd.html', locals())

        # hash md5 加密明文密码
        import hashlib
        m = hashlib.md5()
        m.update(password_1.encode())
        password = m.hexdigest()
        users.password = password
        users.save()
        # 注册成功
        # resp = HttpResponseRedirect('/user/login')
        # resp.set_cookie('username', username, 3600 * 24)
        # resp.set_cookie('uid', user.id, 3600 * 24)
        return render(request,'user/login.html')


def email(request):
    global number
    if request.method == "POST":
        number = random.randint(1000,9999)
        try:
            subject = "大内高手办公系统验证邮件"
            html_message = """
                <p>尊敬的用户 您好</p>
                <p>您的验证码为%s</p>
                """ % (number)
            print("---send email ok---")
            email = request.POST.get("email")
            username = request.POST.get("username")
            print(email)
            users = User.objects.get(username=username)
            if not users:
                # 用户名已注册
                msg = '用户名错误'
                return HttpResponse(msg)
            print(11111111)
            if users.email != email:
                # 用户名已注册
                msg = '邮箱错误'
                return HttpResponse(msg)
            print(2222222)
            send_mail(subject=subject,
                      html_message=html_message,
                      from_email="1075516784@qq.com",
                      recipient_list=[email],
                      message="")
        except Exception as e:
            print("---send email error---")
            print(e)
        return HttpResponse('发送成功')

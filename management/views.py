import datetime
import json
import os

from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from common.Tools import getTimeStamp
from department.models import Department, Position
from management.models import Management
from user.models import User


def management_list(request):
    #获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username = username)[0]
    management = Management.objects.filter(user = user)[0]
    #管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
    department_list = Department.objects.all()
    if management.power == '1':
        power = '1'
        management_list = Management.objects.all()
    else:
        management_list = Management.objects.filter(~Q(job_no = ''))
    return render(request,'management/manager_info.html',locals())

def add_management(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        management = Management.objects.get(id=id)
        job_no = getTimeStamp()
        #只查询有职位的部门
        position_list = Position.objects.values('department').distinct()
        ids = []
        for i in position_list:
            ids.append(i['department'])
        department_list = Department.objects.filter(id__in = ids)

        return render(request,'management/management_add.html',locals())
    elif request.method == 'POST':
        myfile = request.FILES['myfile']

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        file_path = os.path.join(os.path.join(BASE_DIR, 'management/templates/files'), myfile.name)

        with open(file_path, 'wb') as f:
            data = myfile.file.read()
            f.write(data)
        #入职数据插入员工表
        id = request.POST.get('id')
        management = Management.objects.get(id = id)
        #获取前台数据
        #工号
        job_no = request.POST.get('job_no')
        management.job_no = job_no
        #部门
        dep_id = request.POST.get('dep_name')
        dep = Department.objects.get(id = dep_id)
        management.dep_name = dep.name
        #职位
        position_id = request.POST.get('position_name')
        position = Position.objects.get(id = position_id)
        management.position_id = position_id
        management.position_name = position.name
        #姓名
        name = request.POST.get('name')
        management.name = name
        #图片路径
        management.img = '/static/files/'+myfile.name
        #性别
        sex = request.POST.get('sex')
        management.sex = sex
        #入职时间
        create_time = datetime.datetime.now()
        management.create_time = create_time
        management.save()
        # 获取用户名
        username = request.session.get("username")
        user = User.objects.filter(username=username)[0]
        management = Management.objects.filter(user=user)[0]
        # 管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
        department_list = Department.objects.all()
        if management.power == '1':
            power = '1'
            management_list = Management.objects.all()
        else:
            management_list = Management.objects.filter(~Q(job_no=''))
        return render(request, 'management/manager_info.html', locals())


def get_position(request):
    # 获取传入数据
    received_json_data = json.loads(request.body)
    dep_id = received_json_data['dep_id']
    department = Department.objects.get(id=dep_id)
    data = {}
    position_list = Position.objects.filter(department=department)
    data['list'] = json.loads(serializers.serialize("json", position_list))
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})

def get_img(request):
    print("======1========")
    return render(request,'files/a.png')
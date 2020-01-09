import json
import time

from django.shortcuts import render

# Create your views here.
from department.models import Department, Position


def department_list(request):
    position_list = Position.objects.all()
    #分页
    count = len(position_list)
    return render(request,'department/BuMenGL_list.html',locals())

def department_add(request):
    if request.method == 'GET':
        return render(request,'department/BuMenGL_bmtj.html',locals())
    elif request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        description = request.POST.get('description')
        position_name = request.POST.get('position_name')
        if dep_name and description:
            try:
                position_old = Position.objects.filter(name= position_name,dep_name = dep_name)
                if position_old:
                    msg = "已经存在该部门该职位"
                    return render(request, 'department/BuMenGL_bmtj.html', locals())

                dep = Department.objects.create(name= dep_name)
                Department.save(dep)
                position = Position.objects.create(name= position_name,dep_name = dep_name,description = description,
                                                   department = dep)
                Position.save(position)
            except Exception as e:
                print('---添加失败---')
                print(e)
                msg = '添加失败'
                return render(request, 'department/BuMenGL_list.html', locals())
        msg = '添加成功'

        time.sleep(2)
        position_list = Position.objects.all()
        #分页
        count = len(position_list)
        return render(request, 'department/BuMenGL_list.html', locals())

def department_delete(request):

    time.sleep(0.5)
    #获取传入数据
    received_json_data=json.loads(request.body)
    del_position = Position.objects.filter(id=received_json_data['id'])
    del_position.delete()

    #展示页面
    position_list = Position.objects.all()
    #分页
    count = len(position_list)
    return render(request,'department/BuMenGL_list.html',locals())
def department_update(request):

    if request.method == 'GET':
        # 获取传入数据
        id = request.GET.get('id')
        name = request.GET.get('name')
        dep_name = request.GET.get('dep_name')
        description = request.GET.get('description')
        print(id,name,dep_name,description)

        return render(request, 'department/BuMenGL_bmxg.html', locals())
    elif request.method == 'POST':
        #修改数据
        dep_name = request.POST.get('dep_name')
        description = request.POST.get('description')
        position_name = request.POST.get('position_name')
        print(dep_name,'======',position_name)
        #展示页面
        position_list = Position.objects.all()
        #分页
        count = len(position_list)
        return render(request,'department/BuMenGL_list.html',locals())

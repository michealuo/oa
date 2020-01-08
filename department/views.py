import time

from django.shortcuts import render

# Create your views here.
from department.models import Department


def department_list(request):
    department_list = Department.objects.all()
    return render(request,'department/BuMenGL_list.html',locals())

def department_add(request):
    if request.method == 'GET':
        return render(request,'department/BuMenGL_bmtj.html',locals())
    elif request.method == 'POST':
        name = request.POST.get('title')
        description = request.POST.get('description')

        if name and description:
            try:
                dep_old = Department.objects.filter(name= name)
                if dep_old:
                    msg = "已经存在该部门"
                    return render(request, 'department/BuMenGL_bmtj.html', locals())

                dep = Department.objects.create(name= name,description = description)

                Department.save(dep)
            except Exception as e:
                print('---添加失败---')
                print(e)
                msg = '添加失败'
                return render(request, 'department/BuMenGL_list.html', locals())
        msg = '添加成功'

        time.sleep(2)
        return render(request, 'department/BuMenGL_list.html', locals())


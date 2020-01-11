from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from common.Tools import getTimeStamp
from department.models import Department
from management.models import Management
from user.models import User


def management_list(request):
    #获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username = username)[0]
    management = Management.objects.filter(user = user)[0]
    #管理员权限能帮员工入职(看到所有员工),非管理只能看到入职的员工（有工号）
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
        department_list = Department.objects.all()

        return render(request,'management/management_add.html',locals())
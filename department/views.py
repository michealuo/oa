from django.shortcuts import render

# Create your views here.
from department.models import Department


def department_list(request):
    department_list = Department.objects.all()
    print(department_list)
    return render(request,'department/BuMenGL_list.html',locals())
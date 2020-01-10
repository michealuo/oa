from django.shortcuts import render

# Create your views here.
from management.models import Management
from user.models import User


def management_list(request):
    #获取用户名
    username = request.session.get("username")
    user = User.objects.filter(username = username)[0]
    management_list = Management.objects.filter()
    return render(request,'management/manager_info.html')
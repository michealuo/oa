from django.shortcuts import render

# Create your views here.

def management_list(request):
    return render(request,'management/manager_info.html')
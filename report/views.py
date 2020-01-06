from django.shortcuts import render


# Create your views here.

def first_index(request):
    return render(request, "report/index_first.html")


def list(request):
    return render(request, "report/report_list.html")

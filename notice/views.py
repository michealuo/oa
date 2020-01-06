from django.shortcuts import render
from user.models import User


# Create your views here.
def index_view(request):
    uid = request.session.get("uid")
    username = request.session.get("username")
    user = User.objects.get(id=uid, username=username)
    return render(request, "notice/index_first.html", locals())


def notice_view(request):
    return render(request, "notice/notice.html")

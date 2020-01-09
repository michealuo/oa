
from django.shortcuts import render
from .models import *
from index.views import *
# Create your views here.
@logging_check
def timebook_view(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        timebooks = TimeBook.objects.filter(user_id=user_id, ).order_by('-date')

        return render(request, 'timebook/time_book_list.html', locals())
    elif request.method == 'POST':
        date = request.POST.get('date')
        print(date)
        try:
            timebooks = TimeBook.objects.filter(user_id=user_id, date=date)
            print(timebooks)
            return render(request, 'timebook/time_book_list.html', locals())
        except Exception as e:
            timebooks = []
            return render(request, 'timebook/time_book_list.html', locals())
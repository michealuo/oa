from django.conf.urls import url

from department import views

urlpatterns = [
    url(r'^list$',views.department_list),
]
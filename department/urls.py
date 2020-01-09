from django.conf.urls import url

from department import views

urlpatterns = [
    url(r'^list$',views.department_list),
    url(r'^add',views.department_add),
    url(r'^delete',views.department_delete),
    url(r'^update',views.department_update),
]
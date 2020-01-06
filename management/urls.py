from django.conf.urls import url

from management import views

urlpatterns = [
    url(r'^list$',views.management_list),
]
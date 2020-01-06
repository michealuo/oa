from django.conf.urls import url

from report import views

urlpatterns = [
    url(r"^$",views.first_index),
    url(r"^list$",views.list),
    url(r"^add$",views.add),
]

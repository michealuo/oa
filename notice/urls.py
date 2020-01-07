from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list$', views.notice_list),
    url(r'^notice_add$', views.notice_add_view),
    url(r'^notice$', views.notice_view),
]

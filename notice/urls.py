from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^notice$', views.notice),
    url(r'^notice_add$', views.notice_add_view),
    url(r'^notice_view$', views.notice_view),
]

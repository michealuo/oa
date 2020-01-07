from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index_view),
    url('^notice$', views.notice),
    url('^notice_add$', views.notice_add_view),
    url('^notice_view$', views.notice_view),
]

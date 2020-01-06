from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index_view),
    url('^notice$', views.notice_view),
    url('^notice_add$', views.notice_add_view),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index_view),
    url('^notice$', views.notice_view),
]

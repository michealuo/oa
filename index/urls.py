from django.conf.urls import url, include
from django.contrib import admin

from index import views

urlpatterns = [
    url(r'^index', views.index_views),
    url(r'^my_info$', views.index_my_info),
    url(r'^my_ip$', views.index_my_ip),
    url(r'^my_bj$', views.index_my_bj),
    url(r'^my_mim$', views.index_my_mim),
    url(r'^first$',views.index_first_view),
    url(r'^myfirst$',views.myfirst_view),
]
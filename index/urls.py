from django.conf.urls import url, include
from django.contrib import admin

from index import views

urlpatterns = [
    url(r'^index', views.index_views),
    url(r'^index_my$', views.index_my_view),
    url(r'^my_ip$', views.index_my_ip),
    url(r'^my_bj$', views.index_my_bj),
    url(r'^my_mim$', views.index_my_mim),
]
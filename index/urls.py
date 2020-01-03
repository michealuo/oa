from django.conf.urls import url, include
from django.contrib import admin

from index import views

urlpatterns = [
    url(r'^index', views.index_views),
]
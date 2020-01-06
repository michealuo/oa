from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.address_book_view),
    url(r'^YuanGonglist$', views.address_book_list),
]

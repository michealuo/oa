from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^list$',timebook_view),
    url(r'^month$',timebook_month_view),
]
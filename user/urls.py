from django.conf.urls import url

from user import views

urlpatterns =[
    url(r'^login$',views.login_view),
    url(r'^register$',views.reg_view),
    url(r'^logout$',views.logout),
    url(r'^find$',views.findpwd),
    url(r'^email',views.email),

]
from django.conf.urls import url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'login/$', views.login, name='login'),
    url(r'authenticate/$', views.authenticate, name='authenticate'),
    url(r'loginfail/$', views.loginfail, name='loginfail'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'accountdetail/$', views.accountdetail, name='accountdetail'),
    url(r'changepassword/$', views.changepassword, name='changepassword'),
    url(r'changefail/$', views.changefail, name='changefail'),

]

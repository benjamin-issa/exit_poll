from django.conf.urls import url

from . import views

app_name = 'voters'
urlpatterns = [
    url(r'login/$', views.login, name='login'),
]

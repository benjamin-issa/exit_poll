from django.conf.urls import url

from . import views

app_name = 'administration'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

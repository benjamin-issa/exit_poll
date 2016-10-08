from django.conf.urls import url

from . import views

app_name = 'voters'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /voters/5/
    url(r'^(?P<respondent_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<voter_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'randomize/$', views.random, name='random'),
    url(r'result_instructions/$', views.result_page, name='result_page'),
    url(r'instructions/$', views.instructions, name='instructions'),
]
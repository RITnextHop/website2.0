from django.conf.urls import url

from . import views

app_name='nsic'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'sponsors/$', views.Sponsors, name='sponsors'),
]

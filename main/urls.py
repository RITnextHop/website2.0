from django.conf.urls import urls

from . import views

app_name='main'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
]
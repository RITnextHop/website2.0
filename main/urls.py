from django.conf.urls import url

from . import views

app_name='main'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'live/$', views.Live, name='live'),
    url(r'events/$', views.Events, name='events'),
    url(r'^events/(?P<event_url>[\w-]+)/$', views.EventPage, name='event_page'),
    url(r'contact_us/$', views.Events, name='events'),
]
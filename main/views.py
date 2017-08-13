from django.shortcuts import render
from .models import *
import datetime
from django.http import Http404

# Create your views here.

def Index(request):
    data = {
        'current_page': 'Home',
        'eboard': Eboard.objects.get(term='2017-2018'), #update term here to change eboard after creating new eboard db object
        'mission': ClubInfo.objects.get(pk=1).mission,
        'future_events': Event.objects.filter(end_date_time__gt=datetime.datetime.now()).order_by('start_date_time')[:2]
    }
    return render(request,'main/index.html', data)

def Live(request):
    data = {
        'current_page': 'Live',
    }
    return render(request,'main/live.html', data)

def Events(request):
    data = {
        'current_page': 'Events',
        'future_events': Event.objects.filter(end_date_time__gt=datetime.datetime.now()).order_by('start_date_time')
    }
    return render(request,'main/events.html', data)

def EventPage(request, event_url):
    current event = ''
    for event in Event.objects.all():
        if event.url == event_url:
            current_event = event
            break
    if current_event != '':    
        data = {
            'current_page': current_event.title,
            'event': current_event
        }
        return render(request, 'main/event_page.html', data)
    else:
        raise Http404("Event does not exist!")
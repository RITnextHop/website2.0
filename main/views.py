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
    for event in Event.objects.all():
        if event.start_date_time.date() == datetime.date.today():
            data.update({'event_today': event})
            break
    return render(request,'main/index.html', data)

def Live(request):
    data = {
        'current_page': 'Live',
    }
    return render(request,'main/live.html', data)

def Events(request):
    data = {
        'current_page': 'Events',
        'future_events': Event.objects.filter(end_date_time__gt=datetime.datetime.now()).order_by('start_date_time'),
        #have these searches exclude future events?
        'bins': Event.objects.filter(type='Build-It-Night').order_by('start_date_time'),
        'tech_talks': Event.objects.filter(type='Tech Talk').order_by('start_date_time'),
        'other_events': Event.objects.filter(type='Other').order_by('start_date_time'),
    }
    return render(request,'main/events.html', data)

def Contact(request):
    data = {
        'info': ClubInfo.objects.get(pk=1)
    }
    return render(request,'main/contact_us.html',data)

def EventPage(request, event_url):
    current_event = ''
    for event in Event.objects.all():
        if event.url == event_url:
            current_event = event
            break
    if current_event == '':    
        raise Http404("Event does not exist!")
    else:
        data = {
            'current_page': current_event.title,
            'event': current_event
        }
        return render(request, 'main/event_page.html', data)
from django.shortcuts import render
from .models import *
import datetime

# Create your views here.

def Index(request):
    data = {
        'current_page': 'home',
        'eboard': Eboard.objects.get(term='2017-2018'), #update term here to change eboard after creating new eboard db object
        'mission': ClubInfo.objects.get(pk=1).mission,
        'future_events': Event.objects.filter(end_date_time__gt=datetime.datetime.now()).order_by('start_date_time')[:2]
    }
    return render(request,'main/index.html', data)

def Live(request):
    data = {
        'current_page': 'live',
    }
    return render(request,'main/live.html', data)

def Events(request):
    data = {
        'current_page': 'events',
    }
    return render(request,'main/events.html', data)
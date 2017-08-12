from django.shortcuts import render
from .models import *

# Create your views here.

def Index(request):
    data = {
        'current_page': 'home',
        'eboard': Eboard.objects.get(pk=1),
        'mission': ClubInfo.objects.get(pk=1).mission,
    }
    return render(request,'main/index.html', data)
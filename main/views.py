from django.shortcuts import render
from .models import *

# Create your views here.

def Index(request):
    data = {
        'current_page': 'home',
    }
    return render(request,'main/index.html', data)
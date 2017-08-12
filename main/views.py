from django.shortcuts import render
from .models import *

# Create your views here.

def Index(request):
    data = {}
    return render(request,'main/index.html', data)
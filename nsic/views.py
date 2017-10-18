from django.shortcuts import render

from .models import *

# Create your views here.

def Index(request):
    current_year = Year.objects.filter(is_current=True)[:1][0]
    details=NSICInfo.objects.get(pk=1).details.replace('{{ Year.combined_date }}', current_year.combined_date)
    details=details.replace('{{ Year.registration_fee }}', "$"+str(current_year.registration_fee))
    details=details.replace('{{ Year.individual_form }}', current_year.individual_form)
    data = {
        'details': details,
        'NSICInfo': NSICInfo.objects.get(pk=1),
        'Year': current_year,
    }

    return render(request,'nsic/index.html', data)

def Sponsors(request):
    data = {
        'sponsors': Sponsor.objects.all(),
        'partners': Partner.objects.all()
    }

    return render(request, 'nsic/sponsors.html', data)

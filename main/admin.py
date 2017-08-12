from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Doc)
admin.site.register(Event)
admin.site.register(Eboard)
admin.site.register(ClubInfo)
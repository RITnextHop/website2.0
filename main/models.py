from django.db import models

# Create your models here.
class Docs(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

class Event(models.Model):
    EVENT_TYPE = (
        ('bin','Built-It-Night'),
        ('tt','Tech Talk'),
    )
    type = models.CharField(choices=EVENT_TYPE)
    title = models.CharField(max_length=500)
    location models.CharField(max_length=100)
    #get dow from date.weekday()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    description = models.CharField(max_length=10000)
    docs = models.ManyToManyField(Docs)
    steam_url = models.URLField()
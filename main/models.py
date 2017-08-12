from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

class Event(models.Model):
    EVENT_TYPE = (
        (1,'Built-It-Night'),
        (2,'Tech Talk'),
    )
    type = models.IntegerField(choices=EVENT_TYPE, default='1')
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    #get dow from date.weekday()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    description = models.TextField(max_length=10000)
    docs = models.ManyToManyField(Doc)
    steam_url = models.URLField()
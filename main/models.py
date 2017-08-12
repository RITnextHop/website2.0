from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.title

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
    steam_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Eboard(models.Model):
    term = models.CharField(max_length=50, null=True)
    president = models.CharField(max_length=50)
    vice_president = models.CharField(max_length=50)
    secretary = models.CharField(max_length=50)
    treasurer = models.CharField(max_length=50)
    advisor = models.CharField(max_length=50)

    def __str__(self):
        return "{} Term".format(self.term)
    
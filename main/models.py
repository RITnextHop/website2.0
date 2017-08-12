from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Event(models.Model):
    EVENT_TYPE = (
        ('Built-It-Night','Built-It-Night'),
        ('Tech Talk','Tech Talk'),
    )
    type = models.CharField(choices=EVENT_TYPE, default='Built-It-Night', max_length=14)
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    #get dow from date.weekday()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    description = models.TextField(max_length=10000)
    docs = models.ManyToManyField(Doc, blank=True)
    steam_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Eboard(models.Model):
    term = models.CharField(max_length=50, null=True)
    president = models.CharField(max_length=50)
    president_email = models.EmailField()
    president_year_major = models.CharField(max_length=50)
    vice_president = models.CharField(max_length=50)
    vp_email = models.EmailField()
    vp_year_major = models.CharField(max_length=50)
    secretary = models.CharField(max_length=50)
    secretary_email = models.EmailField()
    secretary_year_major = models.CharField(max_length=50)
    treasurer = models.CharField(max_length=50)
    treasurer_email = models.EmailField()
    treasurer_year_major = models.CharField(max_length=50)
    advisor = models.CharField(max_length=50)
    advisor_email = models.EmailField()
    advisor_postion = models.CharField(max_length=50)

    def __str__(self):
        return "{} Term".format(self.term)

class ClubInfo(models.Model):
    mission = models.TextField()
    email = models.EmailField()
    club_page = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return "Club Info"

    class Meta:
        verbose_name_plural = "Club Info"
    
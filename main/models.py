from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='main/docs/')
    #link = models.CharField(max_length=100, help_text='MUST BE IN THIS FORMAT: /docs/SEM_FOLDER/FILE_NAME. ie /docs/Spring_2017/BGPv2.pdf')

    def __str__(self):
        return self.title

class Event(models.Model):
    EVENT_TYPE = (
        ('Build-It-Night','Build-It-Night'),
        ('Tech Talk','Tech Talk',),
        ('Other','Other',),
    )
    type = models.CharField(choices=EVENT_TYPE, default='Build-It-Night', max_length=14)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    description = models.TextField(max_length=10000)
    resources = models.ManyToManyField(Resource, blank=True)
    stream_url = models.URLField(blank=True, help_text='If this is a YouTube link, ensure that /emded/ in include! Example: https://www.youtube.com/embed/EBYrGQoJ0Xg')
    #url_slug = models.SlugField(blank=True)

    @property
    def url(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    self.url_slug = slugify(self.title)
    #    super(Event, self).save(*args, **kwargs)

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
    
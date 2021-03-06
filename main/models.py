from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Resource(models.Model):
    def slugify_file(instance, filename):
        fname, dot, extention = filename.rpartition('.')
        return 'docs/'+slugify(fname)+'.'+extention
    def validate_file_extention(instance):
        if instance.file.content_type != 'application/pdf':
            raise ValidationError(u'File type much be pdf.')
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=slugify_file, validators=[validate_file_extention], help_text='File must be PDF!!!')
    #link = models.CharField(max_length=100, help_text='MUST BE IN THIS FORMAT: /docs/SEM_FOLDER/FILE_NAME. ie /docs/Spring_2017/BGPv2.pdf')

    def __str__(self):
        return self.title

class Event(models.Model):
    EVENT_TYPE = (
        ('Build-It-Night','Build-It-Night'),
        ('Tech Talks','Tech Talks',),
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
    signin_url = models.URLField(blank=True, help_text='Link to Google Form that will only appear when the event is current')

    @property
    def url(self):
        return slugify(self.title)

    @property
    def is_today(self):
        if ((self.start_date_time.date() == timezone.now().date()) and (self.end_date_time >= timezone.now())):
            return True
        else:
            return False
    
    @property
    def is_now(self):
        if self.start_date_time <= timezone.now() <= self.end_date_time:
            return True
        else:
            return False

    @property
    def is_past(self):
        if self.start_date_time <= timezone.now():
            return True
        else:
            return False
    


    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    self.url_slug = slugify(self.title)
    #    super(Event, self).save(*args, **kwargs)

class Eboard(models.Model):
    is_current = models.BooleanField(default=False)
    term = models.CharField(max_length=50, null=True)
    president = models.CharField(max_length=50)
    president_email = models.EmailField()
    president_year_major = models.CharField(max_length=50)
    vice_president = models.CharField(max_length=50)
    vp_email = models.EmailField()
    vp_year_major = models.CharField(max_length=50)
    secretary = models.CharField(max_length=50, blank=True)
    secretary_email = models.EmailField(blank=True)
    secretary_year_major = models.CharField(max_length=50,blank=True)
    treasurer = models.CharField(max_length=50,blank=True)
    treasurer_email = models.EmailField(blank=True)
    treasurer_year_major = models.CharField(max_length=50,blank=True)
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
    
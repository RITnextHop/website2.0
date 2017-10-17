from django.db import models
import datetime

# Create your models here.
class Prize(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class FocusArea(models.Model):
    title = models.CharField(max_length=40)
    detail = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    img = models.ImageField(upload_to='focus_areas/')

    def __str__(self):
        return self.title

class NSICInfo(models.Model):
    what = models.TextField(max_length=1000)
    details = models.TextField(max_length=1000)
    focus_areas = models.ManyToManyField(FocusArea)
    logo = models.ImageField(upload_to='')

    def __str__(self):
        return "NSIC Info"

    class Meta:
        verbose_name_plural = "NSIC Info"

class ScheduleItem(models.Model):
    title = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/')
    url = models.URLField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/')
    url = models.URLField()

    def __str__(self):
        return self.name

class Year(models.Model):
    is_current = models.BooleanField(default=False)
    day1 = models.DateField()
    day2 = models.DateField()
    day1_schedule = models.ManyToManyField(ScheduleItem, related_name='day1_schedule')
    day2_schedule = models.ManyToManyField(ScheduleItem, related_name='day2_schedule')
    prizes = models.ManyToManyField(Prize)
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2)
    sponsors = models.ManyToManyField(Sponsor)
    partners = models.ManyToManyField(Partner)
    possible_topics = models.URLField()
    sign_up_form = models.URLField()
    individual_form = models.URLField()
    volunteer_form = models.URLField()
    mailchimp = models.URLField()
    fb_event = models.URLField()

    def __str__(self):
        return str(self.day1.year)

    @property
    def combined_date(self):
        if self.day1.month != self.day2.month:
            return "{} {} & {} {}, {}".format(self.day1.strftime('%B'),self.day1.day,self.day2.strftime('%B'),self.day2.day,self.day1.year)
        else:
            return "{} {} & {}, {}".format(self.day1.strftime('%B'),self.day1.day,self.day2.day,self.day1.year)


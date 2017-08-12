# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170811_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president', models.CharField(max_length=50)),
                ('vice_president', models.CharField(max_length=50)),
                ('secretary', models.CharField(max_length=50)),
                ('treasurer', models.CharField(max_length=50)),
                ('advisor', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='steam_url',
            field=models.URLField(blank=True),
        ),
    ]

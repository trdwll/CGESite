"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


CLASSES = (
    ('Mercenary', 'Mercenary'),
    ('Sniper', 'Sniper'),
    ('Medic', 'Medic'),
    ('Engineer', 'Engineer'),
)


class HomeData(models.Model):
    about = models.TextField()
    image = models.ImageField()

    class Meta:
        db_table = 'home_data'


class HomeCarousel(models.Model):
    title = models.CharField(max_length=100, help_text='The title on the homepage.')
    tagline = models.CharField(max_length=100, help_text='The tagline that\'s under the title on the homepage.')
    background = models.ImageField(help_text='The image that\'s displayed on the homepage.')
    video_link = models.URLField(help_text='The url for the video that will be on the homepage.', blank=True)

    class Meta:
        db_table = 'home_carousel'


class Character(models.Model):
    character_class = models.CharField(choices=CLASSES, max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField()

    class Meta:
        db_table = 'home_character'

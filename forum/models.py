"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

TOPIC_STATUS = (
    ('1', 'Open'),
    ('2', 'Locked'),
    ('3', 'Pinned'),
)

class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    icon = models.CharField(max_length=20, default='fas fa-comments')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('forum_list_page', kwargs={'forum_slug': self.slug})

    def __str__(self):
        return self.title


class Topic(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='topic_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = RichTextUploadingField()
    #body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='topic_updated_by', on_delete=models.CASCADE, blank=True, null=True)
    updated_reason = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=TOPIC_STATUS, default='Open')

    def get_absolute_url(self):
        return reverse('forum_topic_page', kwargs={'forum_slug': self.forum.slug, 'topic_slug': self.slug, 'topic_id': self.pk})

    def __str__(self):
        return self.title + ' ' + self.author.username


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    body = RichTextUploadingField()
    #body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='post_updated_by', on_delete=models.CASCADE, blank=True, null=True)
    updated_reason = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.topic.title + ' ' + self.author.username


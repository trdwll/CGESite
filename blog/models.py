"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from taggit.managers import TaggableManager

def post_upload_path(instance, filename):
    return 'blog/post/%s/%s' % (instance.slug, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the category.')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_category_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_category'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, help_text='Title of the post.')
    body = RichTextField()
    image = models.ImageField(upload_to=post_upload_path, help_text='The image that will be displayed on the blog home page and on the post itself. (<strong>1280x720</strong>)')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, help_text='The category that the post will be listed under.')
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_post'

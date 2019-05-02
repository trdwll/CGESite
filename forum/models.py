from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('forum_topic_page', kwargs={'forum_slug': self.forum.slug, 'topic_slug': self.slug, 'topic_id': self.pk})

    def __str__(self):
        return self.title + ' ' + self.author.username


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic.title + ' ' + self.author.username


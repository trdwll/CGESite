from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


class Newsletter(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
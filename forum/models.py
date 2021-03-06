from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(User, models.SET_NULL, null=True)

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, models.SET_NULL, null=True)

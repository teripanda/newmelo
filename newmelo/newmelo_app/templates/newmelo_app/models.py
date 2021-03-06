from django.db import models

# // from bootcamp:
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    picture = models.TextField()
    name = models.CharField(max_length=150)
    quote = models.TextField()
    birthday = models.DateField()
    disposition = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.TextField(max_length=500)
    body = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,  related_name='entry')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Gspot(models.Model):
    gspot = models.TextField()
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null = True, blank = True, related_name='gspot')
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

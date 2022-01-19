from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    latitude = models.CharField(max_length=50)
    altitude = models.CharField(max_length=50)
    

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

# class EventMember(models.Model):
#     user = models.ManyToManyField(User)
#     event = models.OneToOneField(Event,on_delete=models.CASCADE)
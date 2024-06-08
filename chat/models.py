from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
#class  User(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Room(models.Model):
    name = models.CharField(max_length=1000)
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
    
    
    
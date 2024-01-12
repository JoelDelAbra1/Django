from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True) # null = true, blank = true, no es obligatorio
   # participants = models.
    updated = models.DateTimeField(auto_now=True) # cada vez que se actualiza
    created = models.DateTimeField(auto_now_add=True) # cuando se crea
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # si se borra el usuario se borran los mensajes
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # si se borra la sala se borran los mensajes
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True) # cada vez que se actualiza
    created = models.DateTimeField(auto_now_add=True) # cuando se crea

    def __str__(self):
        return self.body[:50]

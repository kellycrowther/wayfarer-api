from django.db import models

class Event(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  description = models.TextField()
  time = models.DateTimeField()
  photo = models.TextField()


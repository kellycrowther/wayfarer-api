from django.db import models
from django.core.validators import URLValidator
from waypoints.models import Waypoint

class GuestBook(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  subtitle = models.CharField(max_length=150, blank=True, default='')
  description = models.TextField()
  likes = models.IntegerField(null=True, blank=True)
  coverPhoto = models.TextField(blank=True, default='', validators=[URLValidator()])
  # need to figure out how to add photos to rest framework
  # photos = serializers.ListField(child=serializers.CharField(blank=True, default='', validators=[URLValidator()]))
  
  # figure out how to relate waypoint to guest book
  location = Waypoint()

  def __str__(self):
    return self.title


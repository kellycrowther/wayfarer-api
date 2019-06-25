from django.db import models
from waypoints.models import Waypoint

class Event(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100, blank=True, default='')
  description = models.TextField()
  time = models.DateTimeField()
  photo = models.TextField()
  waypoint_id = models.ForeignKey(Waypoint, related_name='events', blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


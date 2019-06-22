from django.db import models
from django.core.validators import URLValidator

class Waypoints(models.Model):

  WAYPOINT_TYPE_CHOICES = (
    (0, ''),
    (1, 'Urban'),
    (2, 'Country'),
    (3, 'Rural'),
    (4, 'Mountainous'),
    (5, 'Desert'),
    (6, 'Restaurant'),
    (7, 'Park'),
    (8, 'Coffee Shop'),
  )

  # need to figure out multiple choice / many to many relationship
  WAYPOINT_ACTIVITES = (
    (0, ''),
    (1, 'Food'),
    (2, 'Restroom'),
    (3, 'Sightseeing'),
    (4, 'Hiking'),
    (5, 'Photography'),
    (6, 'Nightlife'),
  )

  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  subtitle = models.CharField(max_length=150, blank=True, default='')
  description = models.TextField()
  rating = models.IntegerField()
  favorite = models.IntegerField()
  waypointType = models.IntegerField(choices=WAYPOINT_TYPE_CHOICES, default=0)
  photo = models.TextField(validators=[URLValidator()])
  address = models.TextField()
  state = models.TextField()
  zipCode = models.IntegerField()
  price = models.IntegerField()


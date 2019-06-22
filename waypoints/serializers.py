from rest_framework import serializers
from waypoints.models import Waypoints, WAYPOINT_TYPE_CHOICES, WAYPOINT_ACTIVITES

class WaypointSerializer(serializers.ModelSerializer):
  class Meta:
    model = Waypoints
    fields = ('id', 'title', 'subtitle', 'description', 'rating', 'favorite', 'waypointType', 'photo', 'address', 'state', 'zipCode', 'price')


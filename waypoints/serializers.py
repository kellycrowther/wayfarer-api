from rest_framework import serializers
from waypoints.models import Waypoint, WAYPOINT_TYPE_CHOICES, WAYPOINT_ACTIVITES

class WaypointSerializer(serializers.ModelSerializer):
  class Meta:
    model = Waypoint
    fields = ('id', 'title', 'subtitle', 'description', 'rating', 'favorite', 'waypointType', 'photo', 'address', 'state', 'zipCode', 'price')


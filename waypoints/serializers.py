from rest_framework import serializers
from waypoints.models import Waypoint, WAYPOINT_TYPE_CHOICES, WAYPOINT_ACTIVITES
from events.serializers import EventSerializer

class WaypointSerializer(serializers.ModelSerializer):
  events = EventSerializer(many=True, read_only=True)
  class Meta:
    model = Waypoint
    fields = ('id', 'title', 'subtitle', 'description', 'rating', 'favorite', 'waypointType', 'photo', 'address', 'state', 'zipCode', 'price', 'events')


from rest_framework import serializers
from events.models import Event
from waypoints.serializers import WaypointSerializer

class EventSerializer(serializers.ModelSerializer):
  waypoints = WaypointSerializer(read_only=True)
  class Meta:
    model = Event
    fields = ('id', 'name', 'description', 'time', 'photo', 'waypoints')

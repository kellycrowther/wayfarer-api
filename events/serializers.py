from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
  waypoint_id = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = Event
    fields = ('id', 'name', 'description', 'time', 'photo', 'waypoint_id')

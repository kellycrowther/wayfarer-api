from rest_framework import serializers
from waypoints.models import Waypoint, Coordinate, WAYPOINT_TYPE_CHOICES, WAYPOINT_ACTIVITES
from events.serializers import EventSerializer
from guest_books.serializers import GuestBookSerializer

class CoordinateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coordinate
    fields = ('latitude', 'longitude')

class WaypointSerializer(serializers.ModelSerializer):
  events = EventSerializer(many=True, read_only=True)
  guest_books = GuestBookSerializer(many=True, read_only=True)
  coordinate = CoordinateSerializer(read_only=True)
  class Meta:
    model = Waypoint
    fields = ('id', 'title', 'subtitle', 'description', 'rating', 'favorite', 'waypointType', 'photo', 'address', 'state', 'zipCode', 'price', 'events', 'guest_books', 'coordinate')


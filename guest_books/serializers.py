from rest_framework import serializers
from guest_books.models import GuestBook 

class GuestBookSerializer(serializers.ModelSerializer):
  waypoint_id = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = GuestBook
    fields = ('id', 'title', 'subtitle', 'description', 'likes', 'coverPhoto', 'waypoint_id')

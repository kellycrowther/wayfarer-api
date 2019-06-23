from rest_framework import serializers
from guest_books.models import GuestBook 

# figure out how to serialize location

class GuestBookSerializer(serializers.ModelSerializer):
  class Meta:
    model = GuestBook
    fields = ('id', 'title', 'subtitle', 'description', 'likes', 'coverPhoto')

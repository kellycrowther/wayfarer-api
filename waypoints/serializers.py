from rest_framework import serializers
from waypoints.models import Waypoints, WAYPOINT_TYPE_CHOICES, WAYPOINT_ACTIVITES

class WaypointSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(required=False, allow_blank=True, max_length=100)
  subtitle = serializers.CharField(required=False, allow_blank=True, max_length=150)
  description = serializers.CharField(required=False, allow_blank=True)
  rating = serializers.IntegerField(required=False)
  favorite = serializers.IntegerField(required=False)
  waypointType = serializers.ChoiceField(choices=WAYPOINT_TYPE_CHOICES, default=0)
  photo = serializers.CharField(required=False, allow_blank=True)
  address = serializers.CharField(required=False, allow_blank=True)
  state = serializers.CharField(required=False, allow_blank=True)
  zipCode = serializers.IntegerField(required=False)
  price = serializers.IntegerField(required=False)

  def create(self, validated_data):
    """
      Create and return a new 'Waypoint' instance, given the validated data
    """
    return Waypoints.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
      Update and return an existing 'Waypoint' instance, give the validated data
    """
    instance.title = validated_data.get('title', instance.title)
    instance.subtitle = validated_data.get('subtitle', instance.subtitle)
    instance.description = validated_data.get('description', instance.description)
    instance.rating = validated_data.get('rating', instance.rating)
    instance.favorite = validated_data.get('favorite', instance.favorite)
    instance.waypointType = validated_data.get('waypointType', instance.favorite)
    instance.photo = validated_data.get('photo', instance.photo)
    instance.address = validated_data.get('address', instance.address)
    instance.state = validated_data.get('state', instance.state)
    instance.zipCode = validated_data.get('zipCode', instance.zipCode)
    instance.price = validated_data.get('price', instance.price)
    instance.save()
    return instance



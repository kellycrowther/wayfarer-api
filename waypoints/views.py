from rest_framework import generics
from waypoints.models import Waypoint
from waypoints.serializers import WaypointSerializer


class WaypointList(generics.ListCreateAPIView):
  queryset = Waypoint.objects.all()
  serializer_class = WaypointSerializer

class WaypointDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Waypoint.objects.all()
  serializer_class = WaypointSerializer

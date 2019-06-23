from rest_framework import generics
from waypoints.models import Waypoint
from waypoints.serializers import WaypointSerializer
from rest_framework.permissions import IsAuthenticated


class WaypointList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Waypoint.objects.all()
  serializer_class = WaypointSerializer

class WaypointDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Waypoint.objects.all()
  serializer_class = WaypointSerializer

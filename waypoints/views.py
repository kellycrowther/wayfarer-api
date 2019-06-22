from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from waypoints.models import Waypoint
from waypoints.serializers import WaypointSerializer

@api_view(['GET', 'POST'])
def waypoint_list(request, format=None):
  """
    List all waypoints, or create new waypoint
  """
  if request.method == 'GET':
    waypoints = Waypoint.objects.all()
    serializer = WaypointSerializer(waypoints, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = WaypointSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def waypoint_detail(request, pk, format=None):
  """
    Retrieve, update, or delete a waypoint
  """
  try:
    waypoint = Waypoint.objects.get(pk=pk)
  except Waypoint.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = WaypointSerializer(waypoint)
    return Response(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = WaypointSerializer(waypoint, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    snippet.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


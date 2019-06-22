from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from waypoints.models import Waypoint
from waypoints.serializers import WaypointSerializer

@csrf_exempt
def waypoint_list(request):
  """
    List all waypoints, or create new waypoint
  """
  if request.method == 'GET':
    waypoints = Waypoint.objects.all()
    serializer = WaypointSerializer(waypoints, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def waypoint_detail(request, pk):
  """
    Retrieve, update, or delete a waypoint
  """
  try:
    waypoint = Waypoint.objects.get(pk=pk)
  except Waypoint.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WaypointSerializer(waypoint)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = WaypointSerializer(waypoint, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    snippet.delete()
    return HttpResponse(status=204)


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from waypoints import views

urlpatterns = [
  path('waypoints/', views.waypoint_list),
  path('waypoints/<int:pk>/', views.waypoint_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from waypoints import views

urlpatterns = [
  path('waypoints/', views.waypoint_list),
  path('waypoints/<int:pk>/', views.waypoint_detail),
]

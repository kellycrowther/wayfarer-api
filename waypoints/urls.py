from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from waypoints import views

urlpatterns = [
  path('waypoints/', views.WaypointList.as_view()),
  path('waypoints/<int:pk>/', views.WaypointDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

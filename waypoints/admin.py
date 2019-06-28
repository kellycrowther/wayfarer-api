from django.contrib import admin

from .models import Waypoint, Coordinate

admin.site.register(Waypoint)
admin.site.register(Coordinate)

from django.contrib import admin
from .models import System, LightController, RemoteController, Sensor, Room

admin.site.register(System)
admin.site.register(LightController)
admin.site.register(RemoteController)
admin.site.register(Sensor)
admin.site.register(Room)

# Register your models here.

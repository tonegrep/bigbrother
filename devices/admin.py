from django.contrib import admin
from .models import System, LightController, RemoteController, Sensor

admin.site.register(System)
admin.site.register(LightController)
admin.site.register(RemoteController)
admin.site.register(Sensor)

# Register your models here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from devices.models import *

class IndexView(TemplateView):
    template_name = 'devices.html'
    def get(self, request, *args, **kwargs):
        light_items = LightController.objects.all()
        rc_items = RemoteController.objects.all()
        sensor_items = Sensor.objects.all()
        context = {
        'light_items': light_items,
        'rc_items' : rc_items,
        'sensor_items' : sensor_items,
        }
        return render(request, 'devices.html', context)

# Create your views here.

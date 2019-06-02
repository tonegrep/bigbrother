from django.shortcuts import render
from django.views.generic import TemplateView
from .tasks import process_light, process_sensor
import json
from django.http import HttpResponse

def data_transmit(request):
    if request.method == 'POST':
        
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        controller_type = body['type']
        if controller_type is 0:
            process_light.delay(body)
        elif controller_type is 1:
            process_sensor.delay(body)
        return HttpResponse("ok")
# Create your views here.
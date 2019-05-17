from django.shortcuts import render
from django.views.generic import TemplateView
from .tasks import process_light
import json
from django.http import HttpResponse

def data_transmit(request):
    if request.method == 'POST':
        process_light.delay(json.loads(request.body.decode('utf-8')))
        return HttpResponse("ok")
# Create your views here.
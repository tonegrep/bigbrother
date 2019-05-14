from django.shortcuts import render
from django.views.generic import TemplateView
from .tasks import process_light

def data_transmit(request):
    if request.method == 'POST':
        process_light.delay(request)

# Create your views here.
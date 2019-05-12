from django.shortcuts import render
from django.views.generic import TemplateView
from .celery import 

class HardwareTransmitView(TemplateView):
    def post(self, request):
        pass

# Create your views here.
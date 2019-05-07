from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from devices.models import LightController, RemoteController, Sensor, System, Room
from django.forms import Form, IntegerField, CharField

class LightControllerBrightnessForm(Form):
    controller = CharField(label="item_id")
    brightness = CharField(label="brightness_range")

class LightControllerView(UpdateView):
    def post(self, request, *args, **kwargs):
        #request.get_host() to check if this is server(=server host) or device(= device)
        form = LightControllerBrightnessForm(request.POST)
        print('sha budem zirit')
        if form.is_valid():
            print('paluchilos')
            controller = LightController.objects.get(id=form.data['controller'])
            controller.brightness = form.data['brightness']
            controller.save()
        return redirect('/devices')

class DeviceView(TemplateView):
    template_name = 'devices.html'
    def get(self, request, *args, **kwargs):
        light_items = LightController.objects.filter(system__users=request.user)
        rc_items = RemoteController.objects.filter(system__users=request.user)
        sensor_items = Sensor.objects.filter(system__users=request.user)
        context = {
        'light_items': light_items,
        'rc_items' : rc_items,
        'sensor_items' : sensor_items,
        }
        return render(request, 'devices.html', context)

class ProfileView(TemplateView):
    template_name='profile.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class SystemView(TemplateView):
    template_name = 'system.html'
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.filter(system__users=request.user)
        context = {
            'rooms' : rooms,
        }
        return render(request, 'system.html', context)
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from devices.models import LightController, RemoteController, Sensor, System, Room
from .forms import LightControllerBrightnessForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip

class LightControllerView(UpdateView):
    def post(self, request, *args, **kwargs):
        form = LightControllerBrightnessForm(request.POST)
        print(get_client_ip(request))
        if form.is_valid() or request.POST.get('user_type') == 'controller':
            controller = LightController.objects.get(id=request.POST.get('controller'))
            #ip = controller.system
            controller.brightness = request.POST.get('brightness')
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

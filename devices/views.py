from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from devices.models import LightController, RemoteController, Sensor, System, Room
from .forms import LightControllerBrightnessForm
import requests
from django.utils.decorators import method_decorator

def check_controller_uuid(request):
    pass

# def light_status(request):
#     if request.method == 'POST':
#         controller = LightController.objects.get(uuid=request.GET.get('uuid'))
#         if controller:


class LightControllerBrightnessView(UpdateView):
    def post(self, request, *args, **kwargs):
        form = LightControllerBrightnessForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            brightness = request.POST.get('brightness')
            controller = LightController.objects.get(id=request.POST.get('controller'))
            ip = controller.system.ip
            controller.brightness = brightness
            controller.save()
            controller_response = requests.post('http://' + ip + ':' + str(controller.port) + '/SET',data='brightness=' + brightness)
            print(controller_response)
        return redirect('/devices')

# class RemoteControllerSendSignal(UpdateView):
#     def post(self, request, *args, **kwargs):
#     form = LightControllerBrightnessForm(request.POST)
#     if form.is_valid() and request.user.is_authenticated:
#         brightness = request.POST.get('brightness')
#         controller = LightController.objects.get(id=request.POST.get('controller'))
#         ip = controller.system.ip
#         controller.brightness = brightness
#         controller.save()
#         controller_response = requests.post('http://' + ip + ':' + str(controller.port) + '/SET',data='brightness=' + brightness)
#         print(controller_response)
#     return redirect('/devices')

class DeviceView(TemplateView):
    template_name = 'devices.html'
    def get(self, request, *args, **kwargs):
        light_items = LightController.objects.filter(system__users=request.user)
        # for item in light_items:
        #     if item.id is 2: #change this to if item is available
        #         controller_response = requests.get('http://' + item.system.ip + ':' + str(item.port) + '/GET')
        #         item.brightness = int(controller_response.content)
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

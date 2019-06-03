import requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from devices.models import LightController, RemoteController, Sensor, System, Room, Job
from .forms import LightControllerBrightnessForm, RCSignalForm
import requests
import json
from django.utils.decorators import method_decorator
from devices.actions import SetLightControllerBrightness, SendRemoteControllerSignal
from devices.decorators import create_post_request_entry
from django.contrib import messages
from requests.exceptions import ConnectTimeout
# from abc import ABC, abstractmethod

class WebBrightnessView(UpdateView):
    @method_decorator(create_post_request_entry(LightController, 'brightness'))
    def post(self, request, *args, **kwargs):
        form = LightControllerBrightnessForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            try:
                SetLightControllerBrightness(request.POST.dict())
            except ConnectTimeout:
                messages.error(request, 'Контроллер недоступен. Проверьте, что он включен и имеет доступ к домашней сети.')
        return redirect('/manage')

class WebSignalView(UpdateView):
    def post(self, request, *args, **kwargs):
        form = RCSignalForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            try:
                SendRemoteControllerSignal(request.POST.dict())
            except ConnectionError:
                messages.error(request, 'Контроллер недоступен. Проверьте, что он включен и имеет доступ к домашней сети.')
        return redirect('/manage')

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

class DeviceViewRooms(TemplateView):
    template_name = 'rooms.html'
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.filter(system__users=request.user)
        context = {
            'rooms' : rooms,
        }
        return render(request, 'rooms.html', context)

class SystemView(TemplateView):
    template_name='system.html'
    def get(self, request,*args, **kwargs):
        system_jobs = Job.objects.filter(user = request.user)
        # systems = System.objects.filter(users=request.user)
        # system_jobs = Job.objects.filter(controller__system=systems)
        context = {
            'jobs' : system_jobs,
        }
        return render(request, 'system.html', context)


# Create your views here.

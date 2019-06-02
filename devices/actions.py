from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView
from devices.models import LightController, RemoteController, Sensor, System, Room
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
import json

# def check_controller_uuid(request):
#     pass

class ControllerUpdate(ABC):

    hardware_data_param = None
    response_string = None

    def _hardware_request(self, controller):
        return 'http://' + controller.system.ip + ':' + str(controller.port) + '/SET'

    @abstractmethod
    def _update_field(self, controller, value):
        pass

    def _generic_controller_update(self, controller, value, hardware_request_string, hardware_request_data):
        controller_response = requests.post(hardware_request_string, data=hardware_request_data, timeout=2)
        self._update_field(controller, value)
        controller.save()
        return controller_response

    def _process(self, controller, data):
        hardware_data = self.hardware_data_param + data
        response = self._generic_controller_update(controller, data, self._hardware_request(controller), hardware_data)
        self.response_string = str(response)
        return response
    
    def __str__(self):
        return self.response_string


class SetLightControllerBrightness(ControllerUpdate):
    def __init__(self, request_body):
        self.hardware_data_param = 'brightness='
        controller = LightController.objects.get(id=request_body['controller'])
        brightness = request_body['brightness']
        self._process(controller, brightness)
    
    def _update_field(self, controller, value):
        controller.brightness = value

class SendRemoteControllerSignal(ControllerUpdate):
    def __init__(self, request_body):
        self.hardware_data_param = 'signal='
        controller = RemoteController.objects.get(id=request_body['controller'])
        signal = request_body['signal']
        self._process(controller, signal)

    def _update_field(self, controller, value):
        controller.signal = value

# Create your views here.

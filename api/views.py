from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from .serializers import ControlledDeviceSerializer, RemoteControlCodeSerializer, SystemSerializer, RoomSerializer, LightControllerSerializer, RemoteControllerSerializer, SensorSerializer, JobSerializer, CreateUserSerializer
from devices.models import ControlledDevice, RemoteControlCode, System, Room, LightController, RemoteController, Sensor, Job
import requests

CLIENT_ID = 'SkLYqHz439ZaHl1DntnKrzuEJHv08sAZeZyjOkVc'
CLIENT_SECRET = '8uJg9tl9oAV22HFaQcc2649U6kk4HxoNV3BDs4V5UPQs5AoHm2NlmeRJyL43Z3s95VPE5zS6b2SVFhnQ3oYmOENFFKDovbKcPQDgcP97CDX840jiokZxkEk0UJhJMXVR'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save() 
        r = requests.post('http://192.168.1.10:8000/api/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post(
    'http://192.168.1.10:8000/api/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())

class ControlledDeviceAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = ControlledDevice.objects.get(pk=id)
            serializer = ControlledDeviceSerializer(item)
            return Response(serializer.data)
        except ControlledDevice.DoesNotExist:
            return Response(status=404)

class ControlledDeviceAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = ControlledDevice.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ControlledDeviceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class RemoteControlCodeAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = RemoteControlCode.objects.get(pk=id)
            serializer = RemoteControlCodeSerializer(item)
            return Response(serializer.data)
        except RemoteControlCode.DoesNotExist:
            return Response(status=404)

class RemoteControlCodeAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = RemoteControlCode.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RemoteControlCodeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class SystemAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = System.objects.get(pk=id)
            if request.user in item.users.all():
                serializer = SystemSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except System.DoesNotExist:
            return Response(status=404)

class SystemAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = System.objects.filter(users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SystemSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class RoomAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = Room.objects.get(pk=id)
            if request.user in item.system.users.all():
                serializer = RoomSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except Room.DoesNotExist:
            return Response(status=404)

class RoomAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = Room.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RoomSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class LightControllerAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = LightController.objects.get(pk=id)
            print(item.system.users, request.user)
            if request.user in item.system.users.all():
                serializer = LightControllerSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except LightController.DoesNotExist:
            return Response(status=404)

class LightControllerAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = LightController.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LightControllerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class LightControllerBrightnessAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def post(self, request, format=None):
        try:
            item = LightController.objects.get(pk=request.POST.get('controller'))
            print(item, item.system, item.system.users, request.user)
            if request.user in item.system.users.all():
                ip = item.system.ip
                item.brightness = request.POST.get('brightness')
                item.save()
                requests.post('http://' + ip + ':' + str(item.port) + '/SET',data='brightness=' + request.POST.get('brightness'))
                serializer = LightControllerSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except LightController.DoesNotExist:
            return Response(status=404)

class RemoteControllerAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = RemoteController.objects.get(pk=id)
            if request.user in item.system.users.all():   
                serializer = RemoteControllerSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except RemoteController.DoesNotExist:
            return Response(status=404)

class RemoteControllerAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = RemoteController.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RemoteControllerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class SensorAPIView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, id, format=None):
        try:
            item = Sensor.objects.get(pk=id)
            if request.user in item.system.users.all():
                serializer = SensorSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except Sensor.DoesNotExist:
            return Response(status=404)

class SensorAPIListView(APIView):
    @method_decorator(authentication_classes((TokenAuthentication,SessionAuthentication, OAuth2Authentication,)))
    def get(self, request, format=None):
        items = Sensor.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SensorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
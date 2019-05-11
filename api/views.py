from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ControlledDeviceSerializer, RemoteControlCodeSerializer, SystemSerializer, RoomSerializer, LightControllerSerializer, RemoteControllerSerializer, SensorSerializer, JobSerializer
from devices.models import ControlledDevice, RemoteControlCode, System, Room, LightController, RemoteController, Sensor, Job
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication

@authentication_classes((TokenAuthentication,))
class ControlledDeviceAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = ControlledDevice.objects.get(pk=id)
            serializer = ControlledDeviceSerializer(item)
            return Response(serializer.data)
        except ControlledDevice.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class ControlledDeviceAPIListView(APIView):
    def get(self, request, format=None):
        items = ControlledDevice.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ControlledDeviceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class RemoteControlCodeAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = RemoteControlCode.objects.get(pk=id)
            serializer = RemoteControlCodeSerializer(item)
            return Response(serializer.data)
        except RemoteControlCode.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class RemoteControlCodeAPIListView(APIView):
    def get(self, request, format=None):
        items = RemoteControlCode.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RemoteControlCodeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class SystemAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = System.objects.get(pk=id)
            if item.users is request.user:
                serializer = SystemSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except System.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class SystemAPIListView(APIView):
    def get(self, request, format=None):
        items = System.objects.filter(users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SystemSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class RoomAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Room.objects.get(pk=id)
            if item.system.users is request.user:
                serializer = RoomSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except Room.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class RoomAPIListView(APIView):
    def get(self, request, format=None):
        items = Room.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RoomSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class LightControllerAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = LightController.objects.get(pk=id)
            if item.system.users is request.user:
                serializer = LightControllerSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except LightController.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class LightControllerAPIListView(APIView):
    def get(self, request, format=None):
        items = LightController.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LightControllerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class RemoteControllerAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = RemoteController.objects.get(pk=id)
            if item.system.users is request.user:    
                serializer = RemoteControllerSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except RemoteController.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class RemoteControllerAPIListView(APIView):
    def get(self, request, format=None):
        items = RemoteController.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RemoteControllerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@authentication_classes((TokenAuthentication,))
class SensorAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Sensor.objects.get(pk=id)
            if item.system.users is request.user:
                serializer = SensorSerializer(item)
                return Response(serializer.data)
            return Response(status=401)
        except Sensor.DoesNotExist:
            return Response(status=404)

@authentication_classes((TokenAuthentication,))
class SensorAPIListView(APIView):
    def get(self, request, format=None):
        items = Sensor.objects.filter(system__users=request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SensorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
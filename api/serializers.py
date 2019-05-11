from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from devices.models import ControlledDevice, RemoteControlCode, System, Room, LightController, RemoteController, Sensor, Job

class ControlledDeviceSerializer(ModelSerializer):

    class Meta:
        model = ControlledDevice
        fields = '__all__'


class RemoteControlCodeSerializer(ModelSerializer):

    class Meta:
        model = RemoteControlCode
        fields = '__all__'


class SystemSerializer(ModelSerializer):

    class Meta:
        model = System
        fields = '__all__'


class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class LightControllerSerializer(ModelSerializer):

    class Meta:
        model = LightController
        fields = '__all__'


class RemoteControllerSerializer(ModelSerializer):

    class Meta:
        model = RemoteController
        fields = '__all__'


class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'

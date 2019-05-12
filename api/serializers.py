from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from devices.models import ControlledDevice, RemoteControlCode, System, Room, LightController, RemoteController, Sensor, Job
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

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

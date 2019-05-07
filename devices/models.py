from django.db import models
from django.contrib.auth.models import User
from model_utils.choices import Choices 
from model_utils.fields import StatusField

class ControlledDevice(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=30)

class RemoteControlCode(models.Model):
    device = models.ForeignKey(ControlledDevice, on_delete=models.CASCADE)
    function = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

class System(models.Model):
    name = models.CharField("Smart house", max_length=50)
    address = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    @property
    def get_users(self):
        return users

class Room(models.Model):
    name = models.CharField("Room Name", max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

class Controller(models.Model):
    name = models.CharField("Unknown Controller", max_length=50)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    STATUS = Choices('offline', 'ready', 'busy')
    status = StatusField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, default=None)
    class Meta:
        abstract = True
    def get_users(self):
        return system.get_users()

class LightController(Controller):
    TYPE_CHOICE = Choices('RGB', 'Singlecolor')
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICE,
        default=TYPE_CHOICE.Singlecolor,
    )
    brightness = models.PositiveIntegerField()

class RemoteController(Controller):
    controlled_device = models.ManyToManyField(ControlledDevice)    

class Sensor(Controller):
    MEASURE_CHOICE = Choices('C', '%')
    unit_of_measure = models.CharField(
        max_length=2,
        choices=MEASURE_CHOICE,
        default=MEASURE_CHOICE.C,
    )

class Job(models.Model):
    commands = models.CharField(max_length=200)
    req_date_time = models.DateTimeField(auto_now_add=True)
    RECCURENCE_CHOICE = Choices('Everyday', 'Once')
    reccurence_type = models.CharField(
        max_length=9,
        choices=RECCURENCE_CHOICE,
        default=RECCURENCE_CHOICE.Once,
    )
    reccurence_time = models.TimeField()
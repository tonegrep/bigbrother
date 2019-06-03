from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from model_utils.choices import Choices 
from model_utils.fields import StatusField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    controller_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, default='LightController')
    controller_id = models.PositiveIntegerField(default=0)
    controller = GenericForeignKey('controller_type', 'controller_id')
    datetime = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=100, default='255')

class ControlledDevice(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=30)

class RemoteControlCode(models.Model):
    device = models.ForeignKey(ControlledDevice, on_delete=models.CASCADE)
    function = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

class System(models.Model):
    name = models.CharField("Smart house", max_length=50)
    ip = models.GenericIPAddressField(default=None)
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
    uuid = models.CharField("Unique key of controller", max_length=20, default="X")
    port = models.IntegerField(default=300)
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
    jobs = GenericRelation(Job, related_query_name='lightcontroller')

class RemoteController(Controller):
    controlled_device = models.ManyToManyField(ControlledDevice)    
    jobs = GenericRelation(Job, related_query_name='remotecontroller')

class Sensor(Controller):
    current_data = models.IntegerField(default=0)
    MEASURE_CHOICE = Choices('C', '%')
    unit_of_measure = models.CharField(
        max_length=2,
        choices=MEASURE_CHOICE,
        default=MEASURE_CHOICE.C,
    )
    jobs = GenericRelation(Job, related_query_name='sensor')



    # command = models.CharField(max_length=200)
    # req_date_time = models.DateTimeField(auto_now_add=True)
    # RECCURENCE_CHOICE = Choices('Everyday', 'Once')
    # reccurence_type = models.CharField(
    #     max_length=9,
    #     choices=RECCURENCE_CHOICE,
    #     default=RECCURENCE_CHOICE.Once,
    # )
    # reccurence_time = models.TimeField()
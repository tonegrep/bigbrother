from django.db import models
from django.contrib.auth.models import User

class System(models.Model):
    name = models.CharField("Smart house", max_length=50)
    address = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

class Device(models.Model):
    name = models.CharField("Unknown Device", max_length=50)
    type = models.CharField("General", max_length=50)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

class Light(Device):
    pass
    

class Job(models.Model):
    commands = models.CharField(max_length=200)
    req_date_time = models.DateTimeField(auto_now_add=True)
    EVERYDAY = 'ED'
    ONCE = 'ON'
    RECCURENCE_CHOICE = (
        (EVERYDAY, 'Everyday'),
        (ONCE, 'Once'),
    )
    reccurence_type = models.CharField(
        max_length=2,
        choices=RECCURENCE_CHOICE,
        default=ONCE,
    )
    reccurence_time = models.TimeField()
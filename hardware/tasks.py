from .celery import app
import json
from devices.models import LightController, Sensor
import logging
logger = logging.getLogger(__name__)
# STATUS_READY = 0
# STATUS_BUSY = 1
# STATUS_OFFLINE = 2

STATUS = {
    0 : 'ready',
    1 : 'busy',
    2 : 'offline',
}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip

@app.task
def process_light(info):
    print(info)
    controller = LightController.objects.get(uuid=info['UUID'])
    if controller:
        # ip = get_client_ip(request)
        # if ip != controller.system.ip:
        #     controller.system.ip = ip
        #     controller.system.save()
        controller.brightness = info['data']
        status_code = int(info['status'])
        controller.status = STATUS[status_code]
        print(controller.status)
        controller.save()
    return info['status']

@app.task
def process_sensor(info):
    print(info)
    controller = Sensor.objects.get(uuid=info['UUID'])
    if controller:
        controller.current_data = info['data']['temperature']
        status_code = int(info['status'])
        controller.status = STATUS[status_code]
        controller.save()
    return info['status']
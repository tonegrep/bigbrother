from .celery import app
import json
from devices.models import LightController


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
def process_light(request):
    info = json.loads(request.body.decode('utf-8'))
    controller = LightController.objects.get(uuid=info['UUID'])
    if controller:
        ip = get_client_ip(request)
        if ip != controller.system.ip:
            controller.system.ip = ip
            controller.system.save()
        controller.brightness = info['data']
        controller.status = info['status']
        controller.save()
    return info['status']
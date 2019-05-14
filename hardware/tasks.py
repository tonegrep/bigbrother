from .celery import app
import json
from devices.models import LightController

@app.task
def test(arg):
    logger.info(arg)
    print(arg)
    return arg

@app.task
def process_light(data):
    info = json.loads(data)
    controller = LightController.objects.get(uuid=info['UUID'])
    if controller:
        controller.brightness = info['data']
        controller.status = info['status']
    return info['status']
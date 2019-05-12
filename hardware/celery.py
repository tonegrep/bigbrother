from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import json

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigbrother.settings')

app = Celery('bigbrother')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task
def test(arg):
    logger.info(arg)
    print(arg)
    return arg

@app.task
def process_data(controller_id, data):
    

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test('hello'), name='add every 10')
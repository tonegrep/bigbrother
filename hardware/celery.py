from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigbrother.settings')

app = Celery('bigbrother')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test('hello'), name='add every 10')
from django.urls import include, path, re_path
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from rest_framework.authtoken import views as drf_views

urlpatterns = [
  path('token-auth/', drf_views.obtain_auth_token),
#   re_path(r'^controlleddevice/(?P<id>[0-9]+)$', ControlledDeviceAPIView.as_view()),
#   re_path(r'^controlleddevice/$', ControlledDeviceAPIListView.as_view()),
#   re_path(r'^remotecontrolcode/(?P<id>[0-9]+)$', RemoteControlCodeAPIView.as_view()),
#   re_path(r'^remotecontrolcode/$', RemoteControlCodeAPIListView.as_view()),
  re_path(r'^system/(?P<id>[0-9]+)$', SystemAPIView.as_view()),
  re_path(r'^system/$', SystemAPIListView.as_view()),
  re_path(r'^room/(?P<id>[0-9]+)$', RoomAPIView.as_view()),
  re_path(r'^room/$', RoomAPIListView.as_view()),
  re_path(r'^lightcontroller/(?P<id>[0-9]+)$', LightControllerAPIView.as_view()),
  re_path(r'^lightcontroller/$', LightControllerAPIListView.as_view()),
  re_path(r'^remotecontroller/(?P<id>[0-9]+)$', RemoteControllerAPIView.as_view()),
  re_path(r'^remotecontroller/$', RemoteControllerAPIListView.as_view()),
  re_path(r'^sensor/(?P<id>[0-9]+)$', SensorAPIView.as_view()),
  re_path(r'^sensor/$', SensorAPIListView.as_view()),
#   re_path(r'^job/(?P<id>[0-9]+)$', JobAPIView.as_view()),
#   re_path(r'^job/$', JobAPIListView.as_view()),
]

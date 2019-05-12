from django.contrib import admin
from django.urls import include, path
from devices.views import ProfileView, SystemView
from django.views.decorators.csrf import csrf_exempt
import api.urls

urlpatterns = [
    # path('transmit', HardwareTransmitView.as_view()),
]
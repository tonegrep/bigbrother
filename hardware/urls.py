from django.contrib import admin
from django.urls import include, path
from .views import data_transmit
from django.views.decorators.csrf import csrf_exempt
import api.urls

urlpatterns = [
    path('transmit', csrf_exempt(data_transmit)),
]
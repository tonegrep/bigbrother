from .views import DeviceView, SystemView, ProfileView, WebBrightnessView
from django.urls import include, path

urlpatterns = [
    path('', DeviceView.as_view(), name='manage'),
    path('light_brightness', WebBrightnessView.as_view(), name='light_brightness'),
]
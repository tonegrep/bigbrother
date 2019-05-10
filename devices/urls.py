from .views import DeviceView, SystemView, ProfileView, LightControllerBrightnessView
from django.urls import include, path

urlpatterns = [
    path('', DeviceView.as_view(), name='devices'),
    path('light_brightness', LightControllerBrightnessView.as_view(), name='light_brightness'),
]
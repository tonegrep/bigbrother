"""bigbrother URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from devices.views import DeviceView, SystemView, ProfileView, LightControllerBrightnessView
from .views import HomeView, SignUpView, get_csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('api-token-auth/', drf_views.obtain_auth_token),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', csrf_exempt(SignUpView.as_view()), name='signup'),
    path('devices/', DeviceView.as_view(), name='devices'),
    path('devices/light_brightness', LightControllerBrightnessView.as_view(), name='light_brightness'),
    path('system/', SystemView.as_view(), name='system'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('csrf/', get_csrf, name='csrf'),
]

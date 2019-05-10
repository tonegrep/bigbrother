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
from .views import HomeView, SignUpView, get_csrf
from devices.views import ProfileView, SystemView
from django.views.decorators.csrf import csrf_exempt
import api.urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', csrf_exempt(SignUpView.as_view()), name='signup'),
    path('devices/', include('devices.urls')),
    path('system/', SystemView.as_view(), name='system'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('csrf/', get_csrf, name='csrf'),
]

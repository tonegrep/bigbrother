#from .views import
from django.urls import include, path
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('token-auth/', drf_views.obtain_auth_token),
]
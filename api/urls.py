#from .views import
from django.urls import include, path
from rest_framework.authtoken import views as drf_views
from .views import sample_api

urlpatterns = [
    path('token-auth/', drf_views.obtain_auth_token),
    path('devices/', sample_api)
]
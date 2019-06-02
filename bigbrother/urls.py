from django.contrib import admin
from django.urls import include, path
from .views import HomeView, SignUpView, get_csrf
from web.views import ProfileView, SystemView
from django.views.decorators.csrf import csrf_exempt
import api.urls
from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings

# # OAuth2 provider endpoints
# oauth2_endpoint_views = [
#     path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
#     path('token/', oauth2_views.TokenView.as_view(), name="token"),
#     path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
# ]

urlpatterns = [
    path('api/', include('api.urls')),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', csrf_exempt(SignUpView.as_view()), name='signup'),
    #path('devices/', include('devices.urls')),
    path('manage/', include('web.urls')),
    path('hardware/', include('hardware.urls')),
    path('system/', SystemView.as_view(), name='system'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('csrf/', get_csrf, name='csrf'),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

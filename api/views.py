# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# class ExampleView(APIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

def api_devices(request):
    light_items = LightController.objects.filter(system__users=request.user)
    for item in light_items:
        if item.id is 2: #change this to if item is available
            controller_response = requests.get('http://' + item.system.ip + ':' + str(item.port) + '/GET')
            item.brightness = int(controller_response.content)
    rc_items = RemoteController.objects.filter(system__users=request.user)
    sensor_items = Sensor.objects.filter(system__users=request.user)
    context = {
    'light_items': light_items,
    'rc_items' : rc_items,
    'sensor_items' : sensor_items,
    }
    return render(request, 'devices.html', context)
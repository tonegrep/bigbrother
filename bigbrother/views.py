from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

# Create your views here.

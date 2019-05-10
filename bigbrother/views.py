from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf

def get_csrf(request):
    response = None
    if request.method == 'GET':
        csrf_tok = csrf(request)
        csrf_token =  str(csrf_tok.get('csrf_token'))
    return HttpResponse(response)

class SignUpView(TemplateView):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/signup.html', {'form': form}) 
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

# Create your views here.

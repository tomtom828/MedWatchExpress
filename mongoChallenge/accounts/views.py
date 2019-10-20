from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,FileResponse
from .forms import CustomUserCreationForm, UpdateCustomUser


class CustomSignUp(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    success_message = "Thank you for joining %(username)s!"


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'

def download(request):
    return FileResponse(open('/downloads/FDA-3500_508.pdf','rb'), content_type='application/pdf')

def home(request):
    return render(request, 'core/home.html', {})

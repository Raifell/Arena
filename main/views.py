from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView, ListView
from .forms import CreateUserForm


class MainPageView(TemplateView):
    template_name = 'main/index_main.html'
    extra_context = {
        'title': 'Main Page',
    }

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        return super().get(request, *args, **kwargs)


class LoginPageView(LoginView):
    template_name = 'main/index_login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main_page')
    extra_context = {
        'title': 'Login'
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)


class RegisterPageView(CreateView):
    template_name = 'main/index_register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login_page')
    extra_context = {
        'title': 'Register',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('main_page')

# Create your views here.
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from apps.accounts.forms import RegisterForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from django.contrib.auth import logout
from django.shortcuts import redirect

 
class UserProfileView(TemplateView):
    template_name = 'accounts/user_profile.html'


class RegisterView(CreateView):
    template_name = 'auth/auth_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:registration_sucess')

    def form_valid(self, form):
        response = super().form_valid(form)

        registered_group = Group.objects.get(name='Registered')
        self.object.groups.add(registered_group)

        return response

class LoginView(LoginViewDjango):
    template_name = 'auth/auth_login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('inicio')


class LogoutView(LogoutViewDjango):
    template_name = 'auth/auth_logout.html'
    next_page = reverse_lazy('inicio')
    http_method_names = ['get', 'post']  # Permitir tanto GET como POST
    
    def get(self, request, *args, **kwargs):
        """Mostrar página de confirmación de logout"""
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        """Procesar el logout"""
        if request.user.is_authenticated:
            messages.success(request, '¡Has cerrado sesión correctamente!')
        return super().post(request, *args, **kwargs)

class RegistrationSuccessView(TemplateView):
    template_name = 'auth/registration_success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro Exitoso'
        return context
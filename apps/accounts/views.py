# Create your views here.
from django.contrib import messages
from django.contrib.messages import get_messages
from django.views.generic import TemplateView, CreateView, UpdateView
from apps.accounts.models import User
from apps.accounts.forms import RegisterForm, LoginForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView as LoginViewDjango, LogoutView as LogoutViewDjango
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from django.utils.decorators import method_decorator

 
def is_superuser(user):
    return user.is_superuser

@method_decorator([login_required, user_passes_test(is_superuser)], name='dispatch')
class AdminPanelRedirectView(View):
    def get(self, request):
        # Redirigir a la URL secreta del admin
        return redirect('/sistema-administracion/')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = 'accounts:auth_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        return context

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/profile_edit.html'
    login_url = 'accounts:auth_login'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Limpiar mensajes no relacionados con el perfil
        storage = get_messages(self.request)
        for message in storage:
            # Esto consume/limpia los mensajes existentes
            pass
        return context

class RegisterView(CreateView):
    template_name = 'auth/auth_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Asegurar que el usuario NO tenga permisos de staff
        self.object.is_staff = False
        self.object.is_superuser = False
        self.object.save()

        registered_group = Group.objects.get(name='Registered')
        self.object.groups.add(registered_group)

        login(self.request, self.object)

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
            pass
        return super().post(request, *args, **kwargs)

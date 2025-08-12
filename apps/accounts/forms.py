from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.accounts.models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'alias', 'avatar')
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150, widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu usuario'
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu contraseña'
        })
    )
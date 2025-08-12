from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.accounts.models import User
from django import forms

class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'alias', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password2")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')

        return cleaned_data


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
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
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
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
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu contraseña'
        })
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['alias', 'email', 'avatar']

    # Agregar campos de contraseña
    current_password = forms.CharField(
        label='Contraseña Actual',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña actual'
        }),
        required=False,
        help_text='Requerida solo si quieres cambiar la contraseña'
    )
    
    new_password1 = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        }),
        required=False,
        help_text='Mínimo 8 caracteres'
    )
    
    new_password2 = forms.CharField(
        label='Confirmar Nueva Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma la nueva contraseña'
        }),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
        self.fields['alias'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Alias (opcional)'
        })
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        # Si quiere cambiar contraseña
        if new_password1 or new_password2:
            if not current_password:
                raise forms.ValidationError('Debes ingresar tu contraseña actual para cambiarla.')
            
            # Verificar contraseña actual
            if not self.instance.check_password(current_password):
                raise forms.ValidationError('La contraseña actual es incorrecta.')
            
            # Verificar que las nuevas contraseñas coincidan
            if new_password1 != new_password2:
                raise forms.ValidationError('Las nuevas contraseñas no coinciden.')
            
            # Validar longitud mínima
            if len(new_password1) < 8:
                raise forms.ValidationError('La nueva contraseña debe tener al menos 8 caracteres.')

            return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
    # Si hay nueva contraseña, cambiarla
        new_password1 = self.cleaned_data.get('new_password1')
        if new_password1:
            user.set_password(new_password1)
        
        if commit:
            user.save()
        return user
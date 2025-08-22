from django import forms
from .models import CommentsModel


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribe tu comentario...',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
            })
        }
        labels = {
            'content': ''
        }

# Formulario específico para editar comentarios
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Edita tu comentario...',
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 focus:border-green-400'
            })
        }
        labels = {
            'content': 'Editar comentario'
        }
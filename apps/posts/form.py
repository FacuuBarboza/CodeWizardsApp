from django import forms
from .models import PostsModel


class PostsForm(forms.ModelForm):
    class Meta:
        model = PostsModel
        fields = [
            "cover_img",
            "author",
            "category",
            "title",
            "slug",
            "content",
            "allow_comments",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ingrese un titulo"}),
            "slug": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ingrese un slug"}),
            "content": forms.Textarea(
                attrs={"class": "form-input", "placeholder": "Ingrese un contenido"}),
        }

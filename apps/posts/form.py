from django import forms
from .models import PostsModel


class PostsForm(forms.ModelForm):
    class Meta:
        model = PostsModel
        fields = [
            "cover_img",
            "author",
            "category",
            "city",
            "title",
            "slug",
            "content",
            "event_date",
            "event_time",
            "allow_comments",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ingrese un titulo"}
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ingrese un slug"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-input", "placeholder": "Ingrese un contenido"}
            ),
            "event_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "event_time": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
        }

from django import forms
from .models import CommentsModel


class CommetsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ["content", "user", "post"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "forms-content",
                    "placeholder": "Ingrese un comentario",
                }
            ),
        }

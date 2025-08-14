from django import forms
from apps.comments.models import CommentsModel


class CommetsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ["author", "content"]

        widgets = {
            "author": forms.TextInput(attrs={"class": "from-control"}),
            "content": forms.Textarea(
                attrs={
                    "class": "forms-comments",
                    "placeholder": "Ingrese un comentario",
                }
            ),
        }

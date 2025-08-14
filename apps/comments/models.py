from django.db import models
from apps.posts.models import PostsModel


class CommentsModel(models.Model):
    post = models.ForeignKey(
        PostsModel, related_name="comments", on_delete=models.CASCADE
    )
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author}"


# Create your models here.

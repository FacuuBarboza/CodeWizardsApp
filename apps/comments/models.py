from django.db import models
from apps.posts.models import PostsModel
from django.utils import timezone
from django.conf import settings
import uuid


class CommentsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        PostsModel, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentario de {self.user}"


# Create your models here.

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
import uuid

# from PIL import Image as PilImage
import os


class Category:
    TITLE = {
        "1": "Deporte",
        "2": "Noticias",
        "3": "Aviso",
        "4": "Religion",
        "5": "Fiesta",
        "6": "Invitacio",
        "7": "Otros",
    }


class City:
    TITLE = {
        "1": "Resistencia",
        "2": "Fontana",
        "3": "Saens Peña",
        "4": "Quitilipi",
        "5": "Villa Berthet",
        "6": "Samuhu",
        "7": "Otros",
    }


class PostsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover_img = models.ImageField(default="cover/cover_default.jpg", upload_to="cover/")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=Category.TITLE, default="Otros")
    city = models.CharField(max_length=50, choices=City.TITLE, default="Otros")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("posts_detail", kwargs={"pk": self.pk})


# Create your models here.

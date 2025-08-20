from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
from django.contrib.auth.models import User


class Category:
    TITLE = {
        "Deposte": "Deporte",
        "Noticias": "Noticias",
        "Aviso": "Aviso",
        "Reqligion": "Religion",
        "Fiestas": "Fiesta",
        "Invitacion": "Invitacio",
        "Otros": "Otros",
    }


class City:
    TITLE = {
        "Resistencia": "Resistencia",
        "Fontana": "Fontana",
        "Saenz Peña": "Saens Peña",
        "Quitilipi": "Quitilipi",
        "Villa Berthet": "Villa Berthet",
        "Samuhu": "Samuhu",
        "Otros": "Otros",
    }


class PostsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=Category.TITLE, default="Otros")
    city = models.CharField(max_length=50, choices=City.TITLE, default="Otros")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(
        null=True, blank=True
    )  # Columna para almacenar la hora
    localidad = models.CharField(
        max_length=100, choices=City.TITLE, blank=True, null=True
    )
    cover_img = models.ImageField(default="cover/cover_default.jpg", upload_to="cover/")

    def __str__(self):
        return str(self.author)

    # def get_absolute_url(self):
    #     return reverse("posts_detail", kwargs={"pk": self.pk})

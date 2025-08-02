from BlogCultural.configuraciones.base import *


# En local o desarrollo debe estar en True
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Configuración del puerto para desarrollo
# Este valor puede ser configurado en el entorno o directamente aquí
os.environ["DJANGO_PORT"] = "3000"

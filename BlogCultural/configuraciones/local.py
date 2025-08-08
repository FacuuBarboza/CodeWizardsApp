from BlogCultural.configuraciones.base import *


# En local o desarrollo debe estar en True
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "default_db_name"),
        "USER": os.getenv("DB_USER", "default_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "default_password"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "sql_mode": "traditional",
        }
    }
}

# Configuración del puerto para desarrollo
# Este valor puede ser configurado en el entorno o directamente aquí
os.environ["DJANGO_PORT"] = "3000"

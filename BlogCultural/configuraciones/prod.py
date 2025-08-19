from BlogCultural.configuraciones.base import *


try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:
    pass  # PyMySQL no está instalado, usar configuración por defecto

# En prroduccion debe estar en False
DEBUG = False

# TODO: Configurar el dominio de produccion

ALLOWED_HOSTS = ["facubarboza.pythonanywhere.com"]


# TODO: Configurar la base de datos de produccion
DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        # Descomentar y configurar según la base de datos utilizada
        # "ENGINE": "django.db.backends.postgresql",
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Configuración del puerto para producción
# Este valor puede ser configurado en el entorno o directamente aquí
os.environ["DJANGO_PORT"] = "8080"

import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

DJANGO_ENV = os.getenv("DJANGO_ENV", "local")

if DJANGO_ENV == "production":
    from BlogCultural.configuraciones.prod import *
else:
    from BlogCultural.configuraciones.local import *

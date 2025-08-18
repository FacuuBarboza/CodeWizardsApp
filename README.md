# IMPORTANTE LEER PARA DESPLEGAR PROYECTO

  [Comandos git](#explicación-comandos) | [Crear PR](#6-crear-pull-request) | [Configuracion Inicial](#configuración-inicial) | [Workflow](#workflow-de-desarrollo)

## Blog Cultural - Informatorio 2025

	Proyecto llevado a cabo por el grupo CodeWizardsApp

## Prerrequisitos

- Python 3.8+
- MySQL Server
- Git
## Configuración Inicial
 ### 1 - Clonar repositorio
 

    git clone https://github.com/tunombredeusuario/CodeWizardsApp.git
    cd CodeWizardsApp
   
   

> ⚠️ Cambiar por tu nombre de usuario de git donde dice "tunombredeusuario" para clonar correctamente.

### 2 - Crear entorno virtual
#### 2.a
> El primer 'venv' sería el nombre que quieran darle al entorno

    python -m venv venv
   
#### 2.b
> Para activar el entorno virtual
    
    venv/Scripts/activate
  >⚠️ Donde dice "venv" debe ir el nombre del entorno virtual que escogieron

### 3 - Instalar dependencias
>⚠️ Con el entorno virtual activado

    pip install -r requirements.txt


 ### 4 - Configurar variables de entorno
 >⚠️ Esto para la base de datos(que se crea de forma local para trabajar) y el secret key que genera Django
 

    copy  .env.example  .env
**¿Por qué se usa variables de enviroment?**
Se utilizan para guardar datos sensibles como por ejemplos el usuario de la base de datos y la contraseña. Además del secret key que genera Django así a la hora de subir al repositorio no sepan cual es, ya que se trata de datos sensibles. Se utiliza por seguridad.

### 5 - Generar tu SECRET_KEY personal
> En consola con entorno virtual activado (ver paso 2b)

    python  -c  "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

 
> Se imprimirá por consola el SECRET_KEY, copiar y pegarlo en el archivo '.env' en la variable SECRET_KEY

### 6 - Editar tu archivo .env
```env

SECRET_KEY = "TU_SECRET_KEY_GENERADA"
DEBUG = True

# Configuración de base de datos
DB_NAME = "blog_db" 
DB_USER = "root"
DB_PASSWORD = "tu_password_mysql"
DB_HOST = "localhost"
DB_PORT = "3306"

```
>⚠️ El nombre de db_name debe ser la base de datos creada localmente.
>⚠️ Tanto "db_user" como "db_password" son para trabajar de manera local.
>DB_HOST y DB_PORT dejar así por defecto porque es el que trabaja MySQL

 ### 7 - Crear base de datos
 >Para problemas con mysql, recomiendo instalar completamente descargando el instalador y agregando mysql al PATH de las variables de entorno del sistema si se está trabajando con windows.
 
 

    mysql -u usuarioelegido -p
 >El usuario es el mismo que se configura al instalar mysql siguiendo los pasos. **Por defecto se recomienda usar "root"**
 
 >Luego de lanzado el comando te pide la contraseña utilizada y configurada al instalar mysql con el instalador.
 
 

    CREATE DATABASE blog_db;
    EXIT;
### 8 - Ejecutar migraciones

>Si ya habíamos hecho migraciones en otra base de datos, simplemente eliminando esos archivos es suficiente.

>Ejemplo: Si ya teníamos el archivo "dbsqlite3.db", eliminarlo del proyecto y ejecutar migraciones.

    python manage.py makemigrations
    python manage.py migrate
 
### 9 - Crear superusuario
>Si eliminamos la base de datos que no era mysql, es necesario crear el superusuario de nuevo

>⚠️Hacerlo con entorno virtual activado y en la carpeta del proyecto (Ver paso 2b)
   
    python manage.py createsuperuser
 
### 10 - Ejecutar servidor

    python manage.py runserver

## Estructura para desarrollo

### Crear nuevas apps

>⚠️Con el entorno virtual activado y parado sobre la carpeta: CodeWizardsApp/apps

    python manage.py starapp mi_nueva_app
### Workflow de desarrollo
#### Aclaración
 Si vas a clonar el repo por primera vez e iniciar git. Seguramente se posicione en la rama main que no se debe modificar.
 Seguir estos pasos:
  1. `Git branch`  -- Para ver en que rama estas
  2. `Git checkout development` -- Cambiarse a rama development
  3. `Git pull origin development` -- Si tu rama local está desactualizada de la rama development.
  4. Seguir los pasos de workflow normalmente.
#### 1. Crear rama para el feature que estas por crear: 

    git checkout -b feature/mi-feature

> "feature/mi-feature" es la parte que te tocó desarrollar.
#### 2. Desarrollar tu app 
#### 3. Crear migraciones:
	python manage.py makemigrations
#### 4. Aplicar migraciones
 
    python manage.py migrate
 #### 5. Commit y push

    git status
    git add .

    git commit -m "Realice x cambios"

    git push origin feature/mi-feature

 ##### Explicación comandos:
| Comando| Explicación  |
|--|--|
|  `git init` | Enciende GIT  |
|   `git status`|Es la información del seguimiento de los archivos que están subidos al repositorio remoto. Te aclara cuales se eliminaron y se modificaron y te da aviso de aquellos que no están agregados para el futuro commit.  |
|`git add .`|Agrega todos los archivos que se seguirán para commitear.|
|  `git add archivo.py`| Para agregar algún archivo en específico. |
|`git add *.py`|Para agregar todos aquellos archivos con extensión ".py". Puede ".py" como ".html" o cualquier otra extensión|
|`git add apps/posts`|Para agregar archivos de una carpeta específica|
|`git commit -m 'Mensaje de que se commitea'`|Toma una "foto" de los cambios que has preparado (con `git add`) y los guarda en el historial de tu proyecto. Una versión lista para ser revisada o revertida si es necesario.|
|`git  commit  --amend  -m  "Nuevo mensaje"`|Esto  es para modificar el último commit antes de pushear|
|`git log`|Sirve para ver el historial de commits|
|`git push origin featura/mi-feature`| Esto lleva los cambios que realizaste de manera local (en tu pc) a la rama remota que creaste para desarrollar tu app/funcionalidad. Luego de este comando se podrá visualizar los cambios en la rama creada en github. 'Feature/mi-feature' es el nombre de la rama que creaste.|
|`git pull origin development`| Trae los cambios de la rama de desarrollo a la rama local. Se usa en caso de que tu rama local esté atrasada respecto de la rama remota.|

>⚠️ NUNCA hacer git push origin main

>De cualquier forma saltaría error por reglas del repositorio.

#### 6. Crear Pull Request

	

 1. Ir al repositorio en github.
 2. Ir al apartado "Pull Request".
3. Seleccionar "New Pull Request".
4. En la opciones de ramas(branchs) poner: 
	 **base:development <- compare:tu_rama** 
5. Presionar "Crear Pull Request"
6. Completar formulario con título y descripciones de lo que se quiere agregar. Luego presionar en "Create Pull Request".
7. Dar aviso del PR para que sea revisado y aceptado en caso de no haber errores y/o conflictos.


## 📁 Estructura del proyecto
```
CodeWizardsApp/
├── apps/
│   └── ...              # Irian las apps que creemos
├── BlogCultural/
│   ├── configuraciones/    # Settings por entorno
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── static/                 # Archivos estáticos
├── media/                  # Archivos subidos
├── templates/              # Templates HTML
├── venv/                   # Entorno virtual (no en git)
├── requirements.txt        # Dependencias
├── .env.example           # Variables de entorno ejemplo
├── .gitignore
└── manage.py
```



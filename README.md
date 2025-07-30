# ¡¡IMPORTANTE LEER!!

# BlogCultural - CodeWizards App


## 📋 Descripción
Blog cultural desarrollado con Django para compartir contenido cultural y artístico.

## 🚀 Configuración del entorno de desarrollo

### Prerequisitos
- Python 3.8+
- MySQL 8.0+
- pip
- virtualenv

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/CodeWizardsApp.git
cd CodeWizardsApp/CodeWizardsApp
```

2. **Crear entorno virtual:**
```bash
python3 -m venv venv  
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Configurar base de datos:**
```bash
# Crear base de datos en MySQL
mysql -u root -p
CREATE DATABASE blogcultural_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;

# Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo:**
```bash
python manage.py runserver
```

## 🌿 Flujo de trabajo con Git

### Estructura de branches
```
main (protegida)
├── development (semi-protegida)
    ├── feature/nueva-funcionalidad
    ├── feature/mejora-ui
```

### 1. Iniciar nueva funcionalidad
```bash
# Siempre partir de development actualizado
git checkout development
git pull origin development

# Crear nueva rama feature
git checkout -b feature/nombre-descriptivo

# Trabajar en la funcionalidad
git add .
git commit -m "feat: descripción del cambio"
git push origin feature/nombre-descriptivo
```

### 2. Crear Pull Request
- Ir a GitHub
- Click en "Compare & pull request"
- Seleccionar: `feature/nombre-descriptivo` → `development`
- Llenar template de PR
- Solicitar review de al menos 1 compañero
- ✅ Esperar aprobación ANTES de mergear

## ⚠️ REGLAS IMPORTANTES
- ❌ NUNCA hacer push directo a `main`
- ❌ NUNCA mergear sin review
- ✅ SIEMPRE crear PR para cualquier cambio
- ✅ SIEMPRE actualizar rama antes de crear PR
- ✅ SIEMPRE probar localmente antes de push

### Comandos útiles
```bash
# Crear nueva feature
git checkout development
git pull origin development
git checkout -b feature/nueva-funcionalidad

# Trabajar en la feature
git add .
git commit -m "feat: agregar nueva funcionalidad"
git push origin feature/nueva-funcionalidad

# Crear Pull Request en GitHub
```

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

## 🧪 Testing
```bash
# Ejecutar tests
python manage.py test

# Con coverage
coverage run --source='.' manage.py test
coverage report
```

## 📦 Despliegue
Ver `deploy/` para instrucciones de despliegue en diferentes plataformas.

## 🤝 Contribuir
1. Fork el proyecto
2. Crear feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request


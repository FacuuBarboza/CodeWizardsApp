from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as DjangoUser
from apps.accounts.models import User

# Configurar admin para mostrar solo usuarios superusuario
class CustomUserAdmin(BaseUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # En el admin solo mostrar superusuarios
        return qs.filter(is_superuser=True)

# Desregistrar el modelo User por defecto si está registrado
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Registrar con configuración personalizada
admin.site.register(User, CustomUserAdmin)

# Personalizar textos del admin
admin.site.site_header = 'Panel de Administración - Sistema'
admin.site.site_title = 'Admin Sistema'
admin.site.index_title = 'Administración del Sistema'
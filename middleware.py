from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages

class HideAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Bloquear COMPLETAMENTE la URL /admin/
        if request.path.startswith('/admin/'):
            # Hacer como si la página no existiera
            return HttpResponseNotFound(
                """
                <div style="text-align: center; padding: 50px; font-family: Arial;">
                    <h1>404 - Página no encontrada</h1>
                    <p>La página que buscas no existe.</p>
                    <a href="/">Volver al inicio</a>
                </div>
                """
            )
        
        # Controlar acceso a la ruta secreta del admin
        if request.path.startswith('/sistema-administracion/'):
            # Limpiar mensajes residuales
            storage = messages.get_messages(request)
            for message in storage:
                pass
            
            # Solo permitir superusuarios
            if request.user.is_authenticated and not request.user.is_superuser:
                return HttpResponseForbidden(
                    """
                    <div style="text-align: center; padding: 50px; font-family: Arial;">
                        <h1>🚫 Acceso Denegado</h1>
                        <p>Solo los administradores pueden acceder a esta área.</p>
                        <a href="/">Volver al inicio</a>
                    </div>
                    """
                )
        
        response = self.get_response(request)
        return response
class SeparateAdminAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si accede al admin
        if request.path.startswith('/admin/'):

            storage = messages.get_messages(request)
            for message in storage:
                pass
            
            # Si está autenticado pero NO es superusuario, cerrar sesión y bloquear
            if request.user.is_authenticated and not request.user.is_superuser:
                #logout(request)  # Cerrar sesión automáticamente
                return HttpResponseForbidden(
                    """
                    <div style="text-align: center; padding: 50px; font-family: Arial;">
                        <h1>🚫 Acceso Denegado</h1>
                        <p>Esta área está restringida solo para administradores del sistema.</p>
                        <p>Tu sesión de usuario regular no tiene permisos aquí.</p>
                        <br>
                        <a href="/" style="background: #007cba; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                            🏠 Volver al Sitio Principal
                        </a>
                    </div>
                    """
                )
        
        # Si está en el sitio normal pero viene del admin, mantener separación
        elif not request.path.startswith('/admin/') and request.user.is_authenticated:
            # Verificar que el usuario autenticado sea de tu aplicación, no solo admin
            if request.user.is_superuser and not hasattr(request.user, 'alias'):
                # Es un usuario de admin puro, no debería estar en el sitio normal
                logout(request)
                messages.info(request, 'Sesión de administrador cerrada. Inicia sesión como usuario regular.')
                return redirect('accounts:auth_login')

        response = self.get_response(request)
        return response
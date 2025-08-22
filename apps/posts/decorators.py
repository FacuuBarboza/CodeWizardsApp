from functools import wraps
from django.http import HttpResponseForbidden

def collaborator_required(view_func):
    """
    Decorador para restringir el acceso a usuarios que no son 'Collaborator' o 'Admin'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and (request.user.groups.filter(name__in=['Collaborator', 'Admin']).exists() or request.user.is_superuser):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permisos para acceder a esta página.")
    return _wrapped_view
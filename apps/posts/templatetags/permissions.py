from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def can_manage_comment(user, comment):
    """Verificar si el usuario puede gestionar el comentario"""
    if not user.is_authenticated:
        return False
    
    # Es el autor del comentario
    if user == comment.user:
        return True
    
    # Es staff o superuser
    if user.is_staff or user.is_superuser:
        return True
    
    # Verificar grupos específicos
    user_groups = user.groups.values_list('name', flat=True)
    allowed_groups = ['Collaborators', 'Admin']  # ← Incluir ambas variantes
    
    return any(group in user_groups for group in allowed_groups)

@register.filter
def can_manage_post(user, post):
    """Verificar si el usuario puede gestionar el post"""
    if not user.is_authenticated:
        return False
    
    # Es el autor del post
    if user == post.author:
        return True
    
    # Es staff o superuser
    if user.is_staff or user.is_superuser:
        return True
    
    # Verificar grupos específicos
    user_groups = user.groups.values_list('name', flat=True)
    allowed_groups = ['Collaborators', 'Admin']  # ← Incluir ambas variantes

    
    return any(group in user_groups for group in allowed_groups)

@register.filter
def user_groups(user):
    """Obtener los grupos del usuario como string"""
    if not user.is_authenticated:
        return ""
    return ", ".join(user.groups.values_list('name', flat=True))

@register.filter
def has_group(user, group_name):
    """Verificar si el usuario pertenece a un grupo específico"""
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()
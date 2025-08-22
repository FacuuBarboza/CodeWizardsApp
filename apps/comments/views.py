import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.posts.models import PostsModel
from .models import CommentsModel
from .form import CommentsForm, EditCommentForm

def user_can_manage_comment(user, comment):
    """Función helper para verificar permisos de gestión de comentarios"""
    if not user.is_authenticated:
        return False
    
    # Es el autor del comentario
    if user == comment.user:
        return True
    
    # Es staff o superuser
    if user.is_staff or user.is_superuser:
        return True
    
    # Verificar grupos específicos - NOMBRE CORRECTO: 'Collaborators' (con 's')
    user_groups = user.groups.values_list('name', flat=True)
    allowed_groups = ['Collaborators', 'Admin']
    
    return any(group in user_groups for group in allowed_groups)



@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(PostsModel, id=post_id)
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'comment': {
                        'id': comment.id,
                        'content': comment.content,
                        'user': comment.user.username,
                        'created_at': comment.created_at.strftime('%d/%m/%Y %H:%M')
                    }
                })
            
            #messages.success(request, 'Comentario agregado correctamente.')
            return redirect('posts:post_detail', pk=post_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(CommentsModel, id=comment_id)
    post_slug = comment.post.slug
    
    if request.method == 'POST':
        if user_can_manage_comment(request.user, comment):
            comment.delete()
            #messages.success(request, 'Comentario eliminado correctamente.')
        #else:
            #messages.error(request, 'No puedes eliminar este comentario.')

    return redirect('posts:posts_detail', slug=post_slug)

@login_required
def edit_comment(request, comment_id):
    """View para editar un comentario"""
    comment = get_object_or_404(CommentsModel, id=comment_id)
    
    # Verificar que el usuario es el autor del comentario
    if comment.user != request.user:
        #messages.error(request, "No tienes permisos para editar este comentario.")
        return redirect('posts:posts_detail', slug=comment.post.slug)
    
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.is_edited = True
            form.save()
            #messages.success(request, "Comentario actualizado exitosamente.")
            return redirect('posts:posts_detail', slug=comment.post.slug)
    else:
        form = EditCommentForm(instance=comment)
    
    context = {
        'form': form,
        'comment': comment,
        'post': comment.post
    }
    return render(request, 'posts/edit_comment.html', context)
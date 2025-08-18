# from pyexpat.errors import messages
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404, redirect

# from apps.posts.models import PostsModel
# from .models import CommentsModel
# from .form import CommentsForm

# @login_required
# def add_comment(request, post_id):
#     if request.method == 'POST':
#         post = get_object_or_404(PostsModel, id=post_id)
#         form = CommentsForm(request.POST)
        
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
            
#             if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#                 return JsonResponse({
#                     'success': True,
#                     'comment': {
#                         'id': comment.id,
#                         'content': comment.content,
#                         'user': comment.user.username,
#                         'created_at': comment.created_at.strftime('%d/%m/%Y %H:%M')
#                     }
#                 })
            
#             messages.success(request, 'Comentario agregado correctamente.')
#             return redirect('posts:post_detail', pk=post_id)

# @login_required
# def delete_comment(request, comment_id):
#     comment = get_object_or_404(CommentsModel, id=comment_id)
    
#     # Solo el autor o admin puede eliminar
#     if comment.user == request.user or request.user.has_perm('comments.delete_comment'):
#         post_id = comment.post.id
#         comment.delete()
#         messages.success(request, 'Comentario eliminado.')
#         return redirect('posts:post_detail', pk=post_id)
    
#     messages.error(request, 'No tienes permisos para eliminar este comentario.')
#     return redirect('posts:post_detail', pk=comment.post.id)
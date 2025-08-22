from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .decorators import collaborator_required

from .form import PostsForm
from apps.posts.models import PostsModel
from apps.comments.models import CommentsModel
from apps.comments.form import CommentsForm


def user_can_manage_post(user, post):
    """Función helper para verificar permisos (MISMA LÓGICA que el template tag)"""
    if not user.is_authenticated:
        return False
    
    # Es el autor del post
    if user == post.author:
        return True
    
    # Es staff o superuser
    if user.is_staff or user.is_superuser:
        return True
    
    # Verificar grupos específicos (IGUAL que el template tag)
    user_groups = user.groups.values_list('name', flat=True)
    allowed_groups = ['Collaborator', 'Collaborators', 'Admin']  # ← NOTA: agregué 'Collaborators'
    
    return any(group in user_groups for group in allowed_groups)


def posts_lists(request):
    posts = PostsModel.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})


def posts_detail(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    comments = post.comments.all().order_by('-created_at')
    form = CommentsForm()  # ✅ AGREGAR ESTO
    
    # DEBUG: Imprimir información del usuario
    if request.user.is_authenticated:
        print(f"Usuario: {request.user.username}")
        print(f"Es staff: {request.user.is_staff}")
        print(f"Es superuser: {request.user.is_superuser}")
        print(f"Grupos: {list(request.user.groups.values_list('name', flat=True))}")
        print(f"Es autor: {request.user == post.author}")
        print(f"Puede gestionar: {user_can_manage_post(request.user, post)}")  # ← NUEVO DEBUG

    # Manejar envío de comentarios
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            #messages.success(request, 'Comentario agregado correctamente.')
            return redirect('posts:posts_detail', slug=slug)
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,  
    }
    return render(request, 'posts/posts_detail.html', context)

@login_required
def posts_create(request):
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:posts_detail", slug=post.slug)
    else:
        form = PostsForm()
    return render(request, "posts/posts_form.html", {"form": form})

@login_required
def posts_edit(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)

    # ← USAR LA FUNCIÓN HELPER (igual que el template)
    if not user_can_manage_post(request.user, post):
        print(f"ACCESO DENEGADO - Usuario: {request.user.username}, Puede gestionar: {user_can_manage_post(request.user, post)}")  # ← DEBUG
        messages.error(request, 'No tienes permisos para editar este post.')
        return redirect("posts:posts_detail", slug=slug)
    

    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts_detail', slug=post.slug)
    else:
        form = PostsForm(instance=post)
    return render(request, "posts/posts_form.html", {"form": form})

@login_required
def posts_del(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)

    # ← USAR LA FUNCIÓN HELPER (igual que el template)
    if not user_can_manage_post(request.user, post):
        print(f"ACCESO DENEGADO - Usuario: {request.user.username}, Puede gestionar: {user_can_manage_post(request.user, post)}")  # ← DEBUG
        messages.error(request, 'No tienes permisos para eliminar este post.')
        return redirect("posts:posts_detail", slug=slug)


    if request.method == "POST":
        post.delete()
        return redirect("/")
    return render(request, "posts/posts_delete.html", {"post": post})


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from apps.comments.models import CommentsModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(CommentsModel, id=comment_id)
        
        comment.likes_count += 1
        comment.save()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'likes_count': comment.likes_count,
                'liked': True
            })
        else:
            #messages.success(request, 'Te gusta este comentario.')
            return redirect('posts:posts_detail', slug=comment.post.slug)
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})
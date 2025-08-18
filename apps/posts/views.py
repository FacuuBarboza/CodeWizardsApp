from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .form import PostsForm
from apps.posts.models import PostsModel
from apps.comments.models import CommentsModel
from apps.comments.form import CommentsForm


def posts_lists(request):
    posts = PostsModel.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})


def posts_detail(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    comments = post.comments.all().order_by('-created_at')
    form = CommentsForm()  # ✅ AGREGAR ESTO
    
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


def posts_create(request):
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostsForm()
    return render(request, "posts/posts_form.html", {"form": form})


def posts_edit(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts_detail', slug=post.slug)
    else:
        form = PostsForm(instance=post)
    return render(request, "posts/posts_form.html", {"form": form})


def posts_del(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("/")
    return render(request, "posts/posts_delete.html", {"post": post})


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.comments.models import CommentsModel
from django.views.decorators.csrf import csrf_exempt

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(CommentsModel, id=comment_id)
    post_slug = comment.post.slug
    
    if request.method == 'POST':
        if comment.user == request.user or request.user.is_superuser:
            comment.delete()
            #messages.success(request, 'Comentario eliminado correctamente.')
        #else:
            #messages.error(request, 'No puedes eliminar este comentario.')

    return redirect('posts:posts_detail', slug=post_slug)

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
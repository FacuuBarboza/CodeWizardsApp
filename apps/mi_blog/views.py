from django.shortcuts import render, redirect, get_object_or_404

from apps.posts.form import PostsForm
from apps.posts.models import PostsModel


def my_posts_lists(request):
    posts = PostsModel.objects.all().order_by("-created_at")
    posts_user = []

    # Verifica que solo el usuario con la sesion iniciada actualmente
    # puede acceder a sus propios post para editar, eliminar, etc.
    for post in posts:
        if post.author == request.user:
            posts_user.append(post)
    return render(request, "mi_blog/mi_blog.html", {"posts": posts_user})


# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .form import PostsForm
from apps.posts.models import PostsModel
from apps.comments.models import CommentsModel
from apps.comments.form import CommetsForm


def posts_lists(request):
    posts = PostsModel.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})


def posts_details(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    comments_list = post.comments.all().order_by("-created_at")
    coments_num = post.comments.count()

    paginator = Paginator(comments_list, 5)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    form = CommetsForm()

    if request.method == "POST":
        content = request.POST.get("content")
        CommentsModel.objects.create(post=post, user=request.user, content=content)

        """
        form = CommetsForm(request.POST)
        if form.is_valid():
            form.post = post
            form.save()
            return redirect("/")
        """

    return render(
        request,
        "posts/posts_detail.html",
        {"post": post, "comments": comments, "form": form, "coments_num": coments_num},
    )

    # return render(request, "posts/posts_detail.html", {"post": post})


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
    slug = get_object_or_404(PostsModel, slug=slug)
    if request.method == "POST":
        form = PostsForm(request.POST, instance=slug)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostsForm(instance=slug)
    return render(request, "posts/posts_form.html", {"form": form})


def posts_del(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("/")
    return render(request, "posts/posts_delete.html", {"post": post})

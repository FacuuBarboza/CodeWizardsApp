from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .form import PostsForm
from apps.posts.models import PostsModel
from apps.comments.models import CommentsModel
from apps.comments.form import CommetsForm


def posts_lists(request):
    posts = PostsModel.objects.all().order_by("-created_at")
    return render(request, "index.html", {"posts": posts})


def posts_details(request, slug):
    post = get_object_or_404(PostsModel, slug=slug)
    comments = post.comments.order_by("-created_at")
    form = CommetsForm()

    if request.method == "POST":
        form = CommetsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("detail", slug=post.slug)

    return render(
        request,
        "posts/posts_detail.html",
        {"post": post, "comments": comments, "form": form},
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

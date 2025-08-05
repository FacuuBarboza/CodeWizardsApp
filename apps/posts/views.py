from django.shortcuts import render


def posts_view(request):
    return render(request, "posts/posts.html")


# Create your views here.

from django.shortcuts import render
from apps.posts import views


def index_view(request):
    return views.posts_lists(request)


# def posts(request):
#    return render(request, 'post.html') // se  borra porque en app posts ya lo creamos

from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


# def posts(request):
#    return render(request, 'post.html') // se  borra porque en app posts ya lo creamos

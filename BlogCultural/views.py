from django.shortcuts import render
from apps.posts import views
from django.db.models import Q
from django.apps import apps

def index_view(request):
    return views.posts_lists(request)


# def posts(request):
#    return render(request, 'post.html') // se  borra porque en app posts ya lo creamos

def busqueda_global(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        
        for model in apps.get_models():
            
            text_fields = [f.name for f in model._meta.get_fields() if f.get_internal_type() in ('CharField', 'TextField')]
            
            if text_fields:
                
                q_object = Q()
                for field in text_fields:
                    q_object |= Q(**{f"{field}__icontains": query})
                
                
                queryset = model.objects.filter(q_object)
                
                
                if queryset.exists():
                    resultados.append((model.__name__, queryset))

    return render(request, 'busqueda.html', {'resultados': resultados, 'query': query})

def eventos_view(request):
    return render(request, 'eventos.html')

def lugares_view(request):
    return render(request, 'lugares.html')

def historia_view(request):
    return render(request, 'historia.html')


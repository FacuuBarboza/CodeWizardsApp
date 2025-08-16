from django.shortcuts import render
from apps.posts.models import PostsModel
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


def home(request):
    # Usamos la misma lógica del index para que el buscador funcione en inicio
    return index(request)

def index(request):
    hoy = timezone.now().date()

    query = request.GET.get('q', '')
    localidad = request.GET.get('localidad', '')
    fecha = request.GET.get('fecha', '')

    posts = PostsModel.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if localidad:
        posts = posts.filter(localidad__icontains=localidad)

    if fecha:
        posts = posts.filter(fecha_evento=fecha)

    proximos_eventos = PostsModel.objects.filter(
        fecha_evento__gte=hoy
    ).order_by('fecha_evento')[:6]

    localidades = (
        PostsModel.objects
        .filter(localidad__isnull=False)
        .exclude(localidad__exact='')
        .values_list('localidad', flat=True)
        .distinct()
        .order_by('localidad')
    )

    contexto = {
        'posts': posts,
        'proximos_eventos': proximos_eventos,
        'query': query,
        'localidad': localidad,
        'fecha': fecha,
        'localidades': localidades,
    }

    return render(request, "index.html", contexto)

def busqueda_views(request):
    hoy = timezone.now().date()

    query = request.GET.get('q', '')
    localidad = request.GET.get('localidad', '')
    fecha = request.GET.get('fecha', '')

    resultados = PostsModel.objects.filter(fecha_evento__gte=hoy)

    if query:
        resultados = resultados.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if localidad:
        resultados = resultados.filter(localidad__icontains=localidad)

    if fecha:
        resultados = resultados.filter(fecha_evento=fecha)

    localidades = PostsModel.objects.values_list('localidad', flat=True).distinct()

    contexto = {
        'proximos_eventos': resultados.order_by('fecha_evento'),
        'query': query,
        'localidad': localidad,
        'fecha': fecha,
        'localidades': localidades,
    }

    return render(request, 'busqueda.html', contexto)

def lugares_view(request):
    return render(request, 'lugares.html')

def eventos_view(request):
    return render(request, "eventos.html")

def historia_view(request):
    return render(request, "historia.html")

def nosotros_view(request):
    return render(request, "nosotros.html")

def evento_detail(request, id):
    evento = get_object_or_404(PostsModel, id=id)
    return render(request, "evento_detail.html", {"evento": evento})
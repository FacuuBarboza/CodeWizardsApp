from django.shortcuts import render
from apps.posts.models import PostsModel
from django.utils import timezone
from django.db.models import Q, Count
from django.core.paginator import Paginator
from apps.accounts.models import User
from django.shortcuts import render, get_object_or_404

def home(request):
    # Query base con optimizaciones
    posts = PostsModel.objects.select_related('author').prefetch_related('comments')
    
    # Filtros de búsqueda
    search = request.GET.get('q', '')
    category = request.GET.get('category', '')
    author = request.GET.get('author', '')
    localidad = request.GET.get('localidad', '')
    fecha = request.GET.get('fecha', '')
    
    # Aplicar filtros
    if search:
        posts = posts.filter(
            Q(title__icontains=search) | 
            Q(content__icontains=search) |
            Q(localidad__icontains=search)
        )
    
    if category:
        posts = posts.filter(category=category)
    
    if author:
        posts = posts.filter(author__username=author)
        
    if localidad:
        posts = posts.filter(localidad__icontains=localidad)
    
    if fecha:
        posts = posts.filter(fecha_evento=fecha)
    
    # Anotar con conteos
    posts = posts.annotate(
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    
    # Paginación
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts_page = paginator.get_page(page)
    
    # Datos para filtros
    categories = PostsModel.objects.values_list('category', flat=True).distinct().exclude(category='')
    authors = User.objects.filter(postsmodel__isnull=False).distinct()
    localidades = PostsModel.objects.values_list('localidad', flat=True).distinct().exclude(localidad='')
    
    # Próximos eventos
    hoy = timezone.now().date()
    proximos_eventos = PostsModel.objects.filter(
        fecha_evento__gte=hoy
    ).order_by('fecha_evento')[:6]
    
    context = {
        'posts': posts_page,
        'proximos_eventos': proximos_eventos,
        'categories': categories,
        'authors': authors,
        'localidades': localidades,
        # Mantener valores de filtros para el formulario
        'query': search,
        'category': category,
        'author': author,
        'localidad': localidad,
        'fecha': fecha,
    }
    return render(request, 'index.html', context)

def busqueda_views(request):
    return home(request)

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
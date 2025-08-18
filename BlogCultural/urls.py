from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.views.generic import TemplateView


urlpatterns = [
    path("sistema-administracion/", admin.site.urls),
    path("", views.home, name="inicio"),
    path("posts/", include("apps.posts.urls")),
    path("accounts/", include("apps.accounts.urls")),
    #path("comments/", include("apps.comments.urls")),

    
    path('buscar/', views.busqueda_views, name="busqueda"),
    path('lugares/', views.lugares_view, name="lugares"),
    path('historia/', views.historia_view, name="historia"),
    path('nosotros/', views.nosotros_view, name="nosotros"),
    path('eventos/<uuid:id>/', views.evento_detail, name="evento_detail"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

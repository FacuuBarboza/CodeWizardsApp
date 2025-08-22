from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.views.generic import TemplateView


urlpatterns = [
    path("sistema-administracion/", admin.site.urls),
    path("", views.home, name="inicio"),
    path("mi_blog/", include("apps.mi_blog.urls"), name="mi_blog"),
    path("posts/", include("apps.posts.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("comments/", include("apps.comments.urls")),
    path('mi_blog/', views.miblog, name="mi_blog"),
    path('buscar/', views.busqueda_views, name="busqueda"),
    path('historia/', views.historia_view, name="historia"),
    path('nosotros/', views.nosotros_view, name="nosotros"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

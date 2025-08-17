from django.urls import path
from apps.accounts import views as views
from .views import AdminPanelRedirectView

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/', views.UserProfileEditView.as_view(), name='profile_edit'),
    path('auth/register/', views.RegisterView.as_view(), name='auth_register'),
    path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('admin-panel/', views.AdminPanelRedirectView.as_view(), name='admin_panel'),
]
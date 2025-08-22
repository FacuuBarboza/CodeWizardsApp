from django.urls import path
from apps.posts import views
from apps.mi_blog import views as my_view

#app_name = "mi_blog"

urlpatterns = [
    path("", my_view.my_posts_lists, name="my_posts_lists"),
    path("new/", views.posts_create, name="posts_create"),
    # path("detail/<slug:slug>/", views.posts_details, name="posts_details"),
    path("edit/<slug:slug>/", views.posts_edit, name="posts_edit"),
    path("del/<slug:slug>/", views.posts_del, name="posts_del"),
]

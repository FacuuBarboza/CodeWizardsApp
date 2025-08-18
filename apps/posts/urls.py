from django.urls import path
from apps.posts import views

app_name = "posts"

urlpatterns = [
    path("", views.posts_lists, name="posts_lists"),
    path("new/", views.posts_create, name="posts_create"),
    path("detail/<slug:slug>/", views.posts_detail, name="posts_detail"),
    path("edit/<slug:slug>/", views.posts_edit, name="posts_edit"),
    path("del/<slug:slug>/", views.posts_del, name="posts_del"),

    path('comment/delete/<uuid:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/like/<uuid:comment_id>/', views.like_comment, name='like_comment'),
    # path("posts/<slug:slug>/", views.DetailPostsView.as_view(), name="posts_detail"),
    # path("posts/new/", views.CreatePostsView.as_view(), name="posts_create"),
    # path("posts/edit/<int:pk>/", views.UpdatePostView.as_view(), name="posts_update"),
    # path("posts/del/<int:pk>/", views.DetailPostsView.as_view(), name="posts_delete"),
]

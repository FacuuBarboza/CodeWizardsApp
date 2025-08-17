from django.contrib import admin
from apps.comments.models import CommentsModel
from apps.posts.models import PostsModel

admin.site.register(CommentsModel)
# @admin.register(CommentsModel)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ("post", "user", "content", "created_at")
#     search_fields = ("content", "user__username", "post__title")


# Register your models here.

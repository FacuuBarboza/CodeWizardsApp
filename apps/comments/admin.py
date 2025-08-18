from django.contrib import admin
from apps.comments.models import CommentsModel
from apps.posts.models import PostsModel

@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_at")
    search_fields = ("content", "user__username", "post__title")
    list_filter = ("created_at", "post")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
    list_per_page = 25
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'post')


# Register your models here.

from django.contrib import admin
from .models import Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp']
    search_fields = ['user', 'content']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentModelAdmin)

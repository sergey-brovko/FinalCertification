from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'title', 'body')
    list_editable = ('userId', 'title', 'body')
    list_filter = ('userId',)

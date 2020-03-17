from django.contrib import admin
from .models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_on']
    list_filter = ['author','created_on']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified']
    list_filter = ['created_on','last_modified','categories']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

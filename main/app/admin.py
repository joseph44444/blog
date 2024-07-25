from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_diplay = ["id", "title", "created_at"]
    search_field = ["id", "title", "content"]
    readonly_fields = ["created_at"]
    list_filter = ["created_at"]

class CommentAdmin(admin.ModelAdmin):
    list_diplay = ["id", "comment", "created_at"]
    search_field = ["id", "content"]
    readonly_fields = ["created_at"]
    list_filter = ["created_at"]

class LikeAdmin(admin.ModelAdmin):
    list_diplay = ["id", "comment", "created_at"]
    search_field = ["id", "blog", "like"]
    readonly_fields = ["created_at"]
    list_filter = ["created_at"]

class NewsLetterAdmin(admin.ModelAdmin):
    list_diplay = ["id", "email", "created_at"]
    search_field = ["email"]
    readonly_fields = ["created_at"]
    list_filter = ["created_at"]

admin.site.register(Blog, BlogAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)

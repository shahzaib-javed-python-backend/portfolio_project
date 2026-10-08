from django.contrib import admin
from .models import BlogPost, ContactMessage, Visitor

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path', 'visited_at')
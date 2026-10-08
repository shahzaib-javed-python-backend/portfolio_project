from django.db import models

class Visitor(models.Model):
    ip_address = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} visited {self.path} at {self.visited_at}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, help_text="SEO friendly URL slug")
    meta_description = models.CharField(max_length=160, help_text="Google meta description (max 160 chars)")
    content = models.TextField(help_text="Detailed HTML or Markdown content (1500+ words target)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.contrib import admin
from .models import Post, BlogComment  # added manually

# Register your models here.
admin.site.register(BlogComment)  # added manually

@admin.register(Post)  # added manually
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date', 'url', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

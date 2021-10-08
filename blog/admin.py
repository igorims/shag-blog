from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'author', 'title', 'content', 'publish_date', 'slug', 'is_published')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
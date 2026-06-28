from django.contrib import admin
# Импортируем Project вместе с остальными моделями из файла .models
from .models import Tag, Article, SavedArticle, Comment, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'completion_date']
    list_filter = ['status', 'completion_date']
    search_fields = ['title', 'description']
    list_editable = ['status'] # Удобно менять статус прямо из списка

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_public')
    list_filter = ('is_public', 'pub_date', 'author')
    search_fields = ('title', 'content')
    list_editable = ('is_public',)
    date_hierarchy = 'pub_date'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SavedArticle)
admin.site.register(Comment)

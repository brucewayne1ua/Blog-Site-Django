from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']  # Фильтры на админ панели
    search_fields = ['title', 'body']  # Поле для поиска по заголовку и тексту
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение слага по заголовку
    date_hierarchy = 'publish'  # Иерархия дат для удобного поиска
    raw_id_fields = ['author']  # Поле для поиска автора
    ordering = ['status', 'publish']  # Порядок сортировки записей

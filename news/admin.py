from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    search_fields = ('title',)
    ordering = ('-published_at',)

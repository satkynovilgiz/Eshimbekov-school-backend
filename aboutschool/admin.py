from django.contrib import admin
from .models import AboutBlock

@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    list_display = ('order', 'title')
    ordering = ('order',)

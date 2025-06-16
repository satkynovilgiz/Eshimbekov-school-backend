from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')
    search_fields = ('title',)

    def has_add_permission(self, request):
        return not Banner.objects.exists()

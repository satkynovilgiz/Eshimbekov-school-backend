from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')
    search_fields = ('title',)

    def has_add_permission(self, request):
        # Разрешить добавление, только если нет ни одного баннера
        return not Banner.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Полностью запретить удаление баннера
        return False

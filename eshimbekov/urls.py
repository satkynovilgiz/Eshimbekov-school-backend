from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/gallery/', include('gallery.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/banners/', include('banner.urls')),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', lambda request: JsonResponse({"message": "Welcome to Eshimbekov School API"})),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

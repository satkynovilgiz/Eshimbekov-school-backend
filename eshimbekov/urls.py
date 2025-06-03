from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import NewsListView, NewsDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', NewsListView.as_view(), name='news-list'),
    path('api/news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('api/teachers/', include('teachers.urls')),
    path('api/banners/', include('banner.urls')),  # правильный путь
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

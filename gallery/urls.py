from django.urls import path
from .views import GalleryImageListView, GalleryImageLimitedListView  # <-- импортируем оба класса

urlpatterns = [
    path('', GalleryImageListView.as_view(), name='gallery-list'),
    path('limited/', GalleryImageLimitedListView.as_view(), name='gallery-limit'),  # 3 фото для главной
]

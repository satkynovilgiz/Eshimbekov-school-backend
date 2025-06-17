from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'', VideoViewSet, basename='video')  # ВАЖНО: пустой префикс

urlpatterns = [
    path('', include(router.urls)),
]

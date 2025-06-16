from django.urls import path
from .views import about_blocks_api

urlpatterns = [
    path('', about_blocks_api, name='about_api'),
]

from django.urls import path
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
]

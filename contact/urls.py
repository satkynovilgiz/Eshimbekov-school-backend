from django.urls import path
from .views import send_contact

urlpatterns = [
    path('send/', send_contact, name='send_contact'),
]

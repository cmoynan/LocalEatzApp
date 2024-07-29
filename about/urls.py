from django.urls import path
from .views import about, confirmation

urlpatterns = [
    path('', about, name='about'),
    path('confirmation/', confirmation, name='confirmation'),
]

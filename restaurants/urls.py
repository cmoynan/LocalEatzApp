from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_table/<int:restaurant_id>/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),
]


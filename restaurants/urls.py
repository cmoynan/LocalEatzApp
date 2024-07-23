from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:restaurant_id>/', views.book_table, name='book_table'),
    path('submit_booking/<int:restaurant_id>/', views.submit_booking, name='submit_booking'),
]


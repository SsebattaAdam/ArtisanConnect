# urls.py
from django.urls import path
from . import views



app_name = 'artisan'

urlpatterns = [
    path('register/', views.register_artisan, name='register'),
    path('dashboard/', views.artisan_dashboard, name='dashboard'),
    path('products/add/', views.add_product, name='add_product'),
    path('orders/', views.manage_orders, name='manage_orders'),
]
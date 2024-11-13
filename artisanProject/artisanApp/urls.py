# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'artisan'

urlpatterns = [
    path('register/', views.register_artisan, name='register'),
    path('login/', views.login_artisan, name='login'),  # Login URL
    path('dashboard/', views.artisan_dashboard, name='artisan_dashboard'),
    path('products/add/', views.add_product, name='add_product'),
    path('orders/', views.manage_orders, name='manage_orders'),
]

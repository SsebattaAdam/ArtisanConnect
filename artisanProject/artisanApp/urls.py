
# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
    path('about/', views.about_us, name='about_us'),
    path('get-started/', views.get_started, name='get_started'),
    path('home2/', views.home2, name='home2'),
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]

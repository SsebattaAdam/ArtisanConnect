
# myapp/urls.py
from django.conf import settings
from django.contrib import adminfrom django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
    path('about/', views.about_us, name='about_us'),
    path('home2/', views.home2, name='home2'), 
    path('register_seller/', views.register_seller, name='register_seller'),
    path('login_seller/', views.login_seller, name='login_seller'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('logout_seller/', views.logout_seller, name='logout_seller'),
    path('add_product/', views.add_product, name='add_product'),
    path('forgot-password/', views.forgot_password, name='forgot_password'), 
    path('logout/', views.user_logout, name='user_logout'),
    path('shop/', views.shop, name='shop'),
    path('get-started/', views.get_started, name='get_started'),
    path('home2/', views.home2, name='home2'),
    path('get-started/', views.get_started, name='get_started'),
    path('login_buyer/', views.login_user, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('logout/', views.user_logout, name='user_logout'),
    path('shop/', views.shop, name='shop'),
    path('shop/cart/', views.cart, name='cart'), 
    path('home2/', views.home2, name='home2'), 
    path('register_seller/', views.register_seller, name='register_seller'),
    path('login_seller/', views.login_seller, name='login_seller'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('shop/', views.shop, name='shop'),
    path('shop/', views.shop, name='shop'), 
    path('shop/grid/', views.shop_grid_view, name='shop_grid'),
    path('shop/list/', views.shop_list_view, name='shop_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'), 
    path('contact/', views.contact, name='contact'), 
    path('shop/remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
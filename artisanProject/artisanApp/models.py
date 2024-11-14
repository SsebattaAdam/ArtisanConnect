# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('client', 'Client'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name


class CartItem(models.Model):
    # Linking to the User (customer) who owns the cart
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    
    # Linking to the Product being added to the cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Quantity of this product in the cart
    quantity = models.PositiveIntegerField(default=1)
    
    # Total price for this item (calculated as quantity * price)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Flag to track if the item is still in the cart (useful when checking out)
    in_cart = models.BooleanField(default=True)
    
    # Created and updated timestamps for better tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate total price when saving the item
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

class Cart(models.Model):
    # The cart is linked to a user, as each user has their own cart
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    
    # A cart can have multiple cart items
    cart_items = models.ManyToManyField(CartItem, related_name='cart')
    
    def get_subtotal(self):
        # Calculate the total of all cart items
        return sum(item.total_price for item in self.cart_items.all())
    
    def __str__(self):
        return f"Cart for {self.user.username}"


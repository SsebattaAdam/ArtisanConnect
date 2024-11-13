# models.py
from django.contrib.auth.models import User
from django.db import models
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
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # No user_type here

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'client'  # Set the default user type to client
        if commit:
            user.save()
        return user


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import CustomUser
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.
# myapp/views.py


def home(request):
    return render(request, 'base.html') 


def home2(request):
    return render(request, 'base2.html') 

def about_us(request):
    return render(request, 'aboutUs.html')

def get_started(request):
    return render(request, 'getStarted.html')
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user using username (or email) and password
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid email or password.")  # Add an error message if authentication fails
            
    return render(request, 'login.html')  # Render the login page if not a POST request

def forgot_password(request):
    return render(request, 'forgotPassword.html')


def get_started(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form, user_type is already set to 'client'
            return redirect('home')  # Redirect the user to the home page
    else:
        form = RegistrationForm()
    
    return render(request, 'getStarted.html', {'form': form})


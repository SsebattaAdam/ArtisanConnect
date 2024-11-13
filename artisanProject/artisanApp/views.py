from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from .forms import SellerRegistrationForm, ProductForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from artisanApp.models import CustomUser  # Ensure your CustomUser model is imported
from django.contrib.auth import logout



def home(request):
    return render(request, 'base.html') 

def home2(request):
    return render(request, 'base2.html') 
 
def about_us(request):
    return render(request, 'aboutUs.html')

def get_started(request):
    return render(request, 'getStarted.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'artisans/login.html')

def forgot_password(request):
    return render(request, 'forgotPassword.html')

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('product_list')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'artisans/add_product.html', {'form': form})

def shop(request):
    print("Shop view called")
    return render(request, 'shop.html')

def logout_seller(request):
    logout(request)
    return redirect('login_seller')  # Redirect to the login page after logout

@login_required
def user_logout(request):
    logout(request)
    return redirect('login') 

@login_required
def product_list(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'artisans/product_list.html', {'products': products})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'artisans/edit_product.html', {'form': form, 'product': product})

def register_seller(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'artisans/register.html')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    
    return render(request, 'artisans/register.html')


def login_seller(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('product_list')  # Redirect to product list page on success
        else:
            messages.error(request, "Invalid username or password.")  # Show error if authentication fails
            
    return render(request, 'artisans/login.html')  # Render the login page


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try to get the user by email instead of username
        try:
            user_instance = CustomUser.objects.get(email=email)  # Find user by email
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

        # Authenticate the user using their username (which is the email in this case) and password
        user = authenticate(request, username=user_instance.username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid email or password.")  # Add an error message if authentication fails
            
    return render(request, 'login.html')  # Render the login page if not a POST request

def get_started(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form, user_type is already set to 'client'
            return redirect('home')  # Redirect the user to the home page
    else:
        form = RegistrationForm()
    
    return render(request, 'getStarted.html', {'form': form})
# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import ArtisanRegistrationForm, ProductForm
from .models import Artisan, Product, Order
from django.contrib import messages

def login_artisan(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('artisan:artisan_dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'Artisan/login.html', {'form': form})




def register_artisan(request):
    if request.method == 'POST':
        form = ArtisanRegistrationForm(request.POST)
        if form.is_valid():
            # Create User
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create Artisan
            artisan = form.save(commit=False)
            artisan.user = user
            artisan.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('artisan_dashboard')
    else:
        form = ArtisanRegistrationForm()
    return render(request, 'Artisan/Registration.html', {'form': form})

@login_required(login_url='artisan:login')
def artisan_dashboard(request):
    artisan = get_object_or_404(Artisan, user=request.user)
    products = artisan.products.all()
    orders = artisan.orders.all()
    context = {
        'artisan': artisan,
        'products': products,
        'orders': orders
    }
    return render(request, 'Artisan/Dashboard.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.artisan = request.user.artisan
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('artisan_dashboard')
    else:
        form = ProductForm()
    return render(request, 'artisan/add_product.html', {'form': form})

@login_required
def manage_orders(request):
    artisan = request.user.artisan
    orders = Order.objects.filter(artisan=artisan).order_by('-created_at')
    return render(request, 'artisan/orders.html', {'orders': orders})
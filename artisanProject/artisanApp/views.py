from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from .forms import SellerRegistrationForm, ProductForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Product
from .forms import SellerRegistrationForm, ProductForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from artisanApp.models import CustomUser  # Ensure your CustomUser model is imported
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CartItem
from django.contrib.auth.models import AnonymousUser
from artisanApp.models import CustomUser  # Ensure your CustomUser model is imported
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from .models import CartItem, Product

def home(request):
    # Retrieve all products for display to buyers
    products = Product.objects.all()
    return render(request, 'base.html', {'products': products})
   
def home2(request):
    return render(request, 'base2.html') 
 
 
def about_us(request):
    return render(request, 'aboutUs.html')

def get_started(request):
    return render(request, 'getStarted.html')

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

def forgot_password(request):
    return render(request, 'forgotPassword.html')

def register_seller(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'artisans/register.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login_seller')
        
    return render(request, 'artisans/register.html')

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

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('product_list')

def shop(request):
    print("Shop view called")
    return render(request, 'shop.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login') 

@login_required
def product_list(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'artisans/product_list.html', {'products': products})

def shop(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'shop.html', {'products': products})

def shop_grid_view(request):
    products = Product.objects.all()
    return render(request, 'Shop-Grid.html', {'products': products})  # Match template file name exactly

def shop_list_view(request):
    products = Product.objects.all()
    return render(request, 'Shop-List.html', {'products': products}) 


def checkout(request):
    # You can add logic for the checkout process here (e.g., displaying cart summary, processing payment, etc.)
    return render(request, 'checkout.html')

def wishlist(request):
    return render(request, 'wishlist.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    # Retrieve cart from session or initialize an empty one if not present
    cart = request.session.get('cart', {})

    # Prepare cart items list and calculate total price
    cart_items = []
    total_price = 0

    # Ensure that there are products in the cart and fetch them from the database
    if cart:
        for item_id, item_details in cart.items():
            try:
                # Fetch the product from the database
                product = Product.objects.get(id=item_id)
                
                # Add cart item details to the list
                cart_items.append({
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'quantity': item_details['quantity'],
                    'total_price': product.price * item_details['quantity'],
                    'image': product.image.url,
                })
                total_price += product.price * item_details['quantity']
            except Product.DoesNotExist:
                pass  # Skip or handle missing products if necessary

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    # Debugging cart items and total price
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)

    # Return the rendered cart template with context
    return render(request, 'cart.html', context)

from django.shortcuts import redirect, get_object_or_404
from .models import CartItem  # or the relevant model for cart items

def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id)
        print("Found item:", item)
        item.delete()
    except CartItem.DoesNotExist:
        print("No CartItem found with id:", item_id)
        # You could also redirect or raise an error message here
    return redirect('cart')




from django.contrib import messages

def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)

        if product_id_str in cart:
            cart[product_id_str]['quantity'] += 1
        else:
            cart[product_id_str] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'image': product.image.url,
                'description': product.description,
            }

        request.session['cart'] = cart
        messages.success(request, f"{product.name} added to cart!")
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")

    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.info(request, "Your cart is empty.")
    # You can pass 'cart' to the template to display the items
    return render(request, 'cart.html', {'cart': cart}) 

def user_logout(request):
    logout(request)
    return redirect('home')

def login_user(request):
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
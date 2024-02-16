from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def handle_email_subscription(request, form):
    if form.is_valid():
        email = form.cleaned_data['email']
        if not EmailSubscription.objects.filter(email=email).exists():
            subscription = EmailSubscription(email=email)
            subscription.save()
            messages.success(request, 'Your subscription has been successful!')



def home(request):
    new_release = NewRelease.objects.all().order_by('-id')
    products = Product.objects.all().order_by('-id')
    form = EmailSubscriptionForm()
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        handle_email_subscription(request, form)
    context = {'form': form, 'new_release': new_release, "products": products}
    return render(request, 'home.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                message=form.cleaned_data['message']
            )
            contact_message.save()
            messages.success(
                request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
        else:
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})





def products(request, category_name=None):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()
    selected_category = None
    
    if category_name:
        selected_category = get_object_or_404(Category, name=category_name)
        products = products.filter(category__name=category_name)  #
        
    products_per_page = 6
    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    }
    return render(request, 'product.html', context)


def stores(request):
    stores = Store.objects.all().order_by('-id')
    stores_per_page = 6
    paginator = Paginator(stores, stores_per_page)
    page = request.GET.get('page')
    try:
        stores = paginator.page(page)
    except PageNotAnInteger:
        stores = paginator.page(1)
    except EmptyPage:
        stores = paginator.page(paginator.num_pages)
    context = {'stores': stores}
    return render(request, 'store.html', context)


def product_details(request, product_name=None):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product_details.html', {'product': product})



def cart(request):
    cart_items = request.session.get('cart', {})
    product_ids = cart_items.keys()
    products_in_cart = Product.objects.filter(id__in=product_ids)    
    total_price = sum(cart_items[str(product.id)] * product.price for product in products_in_cart)
    total_items_in_cart = sum(cart_items.values())
    context = {
        'products_in_cart': products_in_cart,
        'total_price': total_price,
        'total_items_in_cart': total_items_in_cart  
    }
    return render(request, 'cart.html', context)



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.user.is_authenticated:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.filter(product=product)
    else:
        cart = request.session.get('cart', {})
    
    if request.user.is_authenticated:
        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=1)
    else:
        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1
        request.session['cart'] = cart
    messages.success(request, 'Product added to cart successfully!')
    return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.filter(product=product)
    else:
        cart = request.session.get('cart', {})
        cart_quantity = cart.get(str(product_id), 0)
    if request.user.is_authenticated:
        if cart_items.exists():
            cart_item = cart_items.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
    elif cart_quantity > 1:
        cart[str(product_id)] = cart_quantity - 1
        request.session['cart'] = cart
    elif cart_quantity == 1:
        del cart[str(product_id)]
        request.session['cart'] = cart
    messages.success(request, 'Product removed from cart successfully!')
    return redirect('cart')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'authentication/reset_password.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/reset_password_complete.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
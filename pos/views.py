from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        products = products.filter(categories__in=[category])
    products_per_page = 6
    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'products': products, 'categories': categories,
               'selected_category': category_name}
    return render(request, 'product.html', context)


def product_details(request, product_name=None):
    product = get_object_or_404(Product, name=product_name)

    return render(request, 'product_details.html', {'product': product})

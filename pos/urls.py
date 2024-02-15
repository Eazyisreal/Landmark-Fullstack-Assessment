from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('product', views.products, name='products'),
    path('product_details/<str:product_name>/', views.product_details, name='product_details'),
    path('product/<str:category_name>/', views.products, name='all_products'),
    
]
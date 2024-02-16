from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Cart, CartItem

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', price=10, quantity=5, category=self.category)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200) 

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_product_details_view(self):
        response = self.client.get(reverse('product_details', args=[self.product.name]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)  

    def test_add_to_cart_view(self):

        self.client.force_login(self.user)  
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  

    def test_remove_from_cart_view(self):
        self.client.force_login(self.user)  
        response = self.client.post(reverse('remove_from_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200) 
        response = self.client.post(reverse('contact'), {'name': 'Test User', 'email': 'test@example.com', 'message': 'Test message'})
        self.assertEqual(response.status_code, 302)  

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)  

    def test_custom_password_reset_view(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)  


    def test_stores_view(self):
        response = self.client.get(reverse('stores'))
        self.assertEqual(response.status_code, 200)  

    def test_stores_view(self):
        response = self.client.get(reverse('stores'))
        self.assertEqual(response.status_code, 200) 

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)  
        response = self.client.post(reverse('contact'), {'name': 'Test User', 'email': 'test@example.com', 'message': 'Test message'})
        self.assertEqual(response.status_code, 302)  

    def test_custom_password_reset_views(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200) 
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)



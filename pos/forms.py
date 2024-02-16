from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    username = forms.CharField(max_length=100, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ContactForm(forms.Form):
    name = forms.CharField( max_length=100)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=False) 
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        
        
class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField()


    
class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
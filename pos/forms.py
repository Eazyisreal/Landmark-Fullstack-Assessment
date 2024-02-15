from django import forms

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
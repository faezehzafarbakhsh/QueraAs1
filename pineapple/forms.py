from django import forms
from .models import Subscription
import re
from django.core.exceptions import ValidationError
class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields=['name','phone_number']
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_re=r'^09\d{9}$'
        if not re.match(phone_re,phone_number):
            raise forms.ValidationError("شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.")
        return phone_number
            
        
        
    
       

class CommentForm:
    pass
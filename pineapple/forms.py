from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import *

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name' , 'address', 'certificate_code']
        
    def clean_address(self):
        address = self.cleaned_data.get('address')
        
        if len(address) < 10:
            raise ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return address
    
    def clean_certificate_code(self):
        certificate_code = self.cleaned_data.get('certificate_code')
        
        if certificate_code.isupper() == False:
            raise ValidationError('حروف گواهینامه باید حروف بزرگ باشد.')
        return certificate_code
    

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm:
    pass

class CommentForm:
    pass
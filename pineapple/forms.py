from django import forms
from .models import Subscription
import re
class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pass

# class SubscriptionForm:
    
#         phone_regex = r'^09\d{9}$'
#         if not re.match(phone_regex, phone_number):
#             raise forms.ValidationError('شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')
#         return phone_number

class CommentForm:
    pass
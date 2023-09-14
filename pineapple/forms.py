from django import forms
from . import models
from django.core.exceptions import ValidationError

class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['pineapple', 'name', 'weight_kg']

    def clean_weight_kg(self):
        weight = self.cleaned_data.get('weight_kg')
        if weight > 100:
            raise ValidationError('شما تنها می‌توانید حداکثر 100 کیلوگرم آناناس سفارش دهید.')
        return weight


class SubscriptionForm:
    pass

class CommentForm:
    pass
from . import models
from django import forms
from django.core.exceptions import ValidationError


class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm:
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text','name','seller']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return text
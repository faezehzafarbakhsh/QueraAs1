from . import models
from django import forms
from django.core.exceptions import ValidationError


class SellerForm:
    pass

class PineappleForm(forms.ModelForm):

    class Meta:
        model = models.Pineapple
        fields = ['price_toman', 'seller']

    def clean_price_toman(self):
        price = self.cleaned_data.get('price_toman')
        if price < 1000:
            raise ValidationError('قیمت نباید کمتر از هزار تومان باشد.')
        if price > 1000000:
            raise ValidationError('قیمت نباید از یک میلیون تومان بیشتر باشد.')

        return price

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
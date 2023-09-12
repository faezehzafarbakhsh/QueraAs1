from django import forms

class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pineapple_weight = forms.IntegerField(label='وزن آناناس (کیلوگرم)')
    def clean_pineapple_weight(self):
        weight = self.cleaned_data['pineapple_weight']
        if weight > 100:
            raise forms.ValidationError('شما تنها می‌توانید حداکثر ۱۰۰ کیلوگرم آناناس سفارش دهید.')
        return weight


class SubscriptionForm:
    pass

class CommentForm:
    pass
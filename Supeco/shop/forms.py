from django import forms

from shop.models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['name', 'phone', 'email', 'status']

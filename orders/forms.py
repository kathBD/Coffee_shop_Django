from django.forms import ModelForm
from django import forms
from .models import OrderProduct

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']  # Include 'quantity' if needed



class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
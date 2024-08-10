from django.forms import ModelForm
from django import forms
from .models import OrderProduct

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']  # Include 'quantity' if needed
        widgets = {
            'product': forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'}),
        }



class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
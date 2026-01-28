from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': ''}),
            'email': forms.EmailInput(attrs={'placeholder': ' '}),
            'address': forms.TextInput(attrs={'placeholder': ''}),
            'postal_code': forms.TextInput(attrs={'placeholder': ''}),
            'city': forms.TextInput(attrs={'placeholder': ' '}),
        }
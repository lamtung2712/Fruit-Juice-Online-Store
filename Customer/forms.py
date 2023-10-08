from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

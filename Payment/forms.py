# trong file forms.py
from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date', input_formats=['%m/%Y'])
    cvv = forms.CharField(label='CVV', max_length=3)

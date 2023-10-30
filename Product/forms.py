from django import forms

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False)
    category = forms.CharField(required=False)


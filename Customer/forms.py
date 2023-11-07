from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Xác nhận mật khẩu'}))

    class Meta:
        model = Customer
        fields = ['customer_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Mật khẩu và xác nhận mật khẩu không trùng khớp.")

    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({'placeholder': 'Họ và tên'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})


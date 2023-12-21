from django import forms
from django.contrib.auth.models import  Permission, Group, User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, AuthenticationForm

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    class Meta:
        model: User
        fields = ('username', 'password')



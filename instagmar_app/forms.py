from django import forms
from django.core import validators
from .models import UserModel


class LoginForm(forms.ModelForm):
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Mobile Number Or Email'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserModel
        fields = '__all__'


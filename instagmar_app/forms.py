from django import forms
from django.core import validators
from .models import UserModel


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserModel
        fields = '__all__'


class LoginForm(forms.Form):

    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


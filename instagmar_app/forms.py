from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .models import MyUser, Post


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = MyUser
        fields = ('email', 'fullname', 'username', 'password')


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

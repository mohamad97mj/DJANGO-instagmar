from django.shortcuts import render
from . import forms

# Create your views here.


def signupview(request):
    signup_form = forms.SignUpForm()
    context = {'signup_form': signup_form}
    return render(request, 'instagmar_app/signup_page.html', context=context)
    # return render(request, 'instagmar_app/test.html', context=context)


def loginview(request):
    login_form = forms.LoginForm()
    context = {'login_form': login_form}
    return render(request, 'instagmar_app/login_page.html', context=context)

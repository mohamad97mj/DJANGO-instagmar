from django.shortcuts import render
from . import forms

# Create your views here.


def loginview(request):
    login_form = forms.LoginForm()
    context = {'login_form': login_form}
    return render(request, 'instagmar_app/instagmar_login.html', context=context)


from django.shortcuts import render
from . import forms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User


def signupview(request):
    signedup = False

    if request.method == "POST":
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            signedup = True

        else:
            print(signup_form.errors)

    else:
        signup_form = forms.SignUpForm()

    context = {'signup_form': signup_form, 'signedup': signedup}

    return render(request, 'instagmar_app/signup_page.html', context=context)


@login_required
def homeview(request):
    return render(request, 'instagmar_app/home_base.html', context={})


def testview(request):
    return render(request, 'instagmar_app/test.html', context={})


def loginview(request):
    login_form = forms.LoginForm()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            print("authenticated again and again")

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('instagmar_app:homeview'))

            else:
                return HttpResponse("account not activate")

        else:
            print("someone tried to login and failed")
            return HttpResponse("invalid login details supplied!")

    else:
        context = {'login_form': login_form}
        return render(request, 'instagmar_app/login_page.html', context=context)


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('instagmar_app:signupview'))


def postsview(request):
    return render(request, 'instagmar_app/posts_page.html', context={})

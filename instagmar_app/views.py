from itertools import chain

from django.shortcuts import render
from . import forms
from . import models

from django.utils import timezone
from operator import attrgetter
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'instagmar_app/chatindex.html', {})


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


def getthisuser(request):
    username = request.session.get('username')
    this_user = models.MyUser.objects.get(username=username)
    return this_user


@login_required
def mainview(request):
    this_user = getthisuser(request)
    post_set = this_user.post_set.order_by('datetime')
    context = {'this_user': this_user, 'post_set': post_set}
    return render(request, 'instagmar_app/instagmar_page.html', context=context)


def baseview(request):
    return render(request, 'instagmar_pp/base.html', context={})


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
                request.session['username'] = user.username
                return HttpResponseRedirect(reverse('instagmar_app:mainview'))

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


@login_required
def postsview(request):
    this_user = getthisuser(request)
    post_list = this_user.post_set.all()

    for following in this_user.followings.all():
            post_list = sorted(chain(post_list.all(), following.post_set.all()), key=attrgetter('datetime'))

    print("dates are:")
    for post in post_list:
        print(post.datetime)

    context = {'this_user': this_user, 'post_list': post_list}
    return render(request, 'instagmar_app/posts_page.html', context=context)


@login_required
def newpostview(request):
    if request.method == 'POST':
        this_user = getthisuser(request)
        content = request.FILES['content']
        caption = request.POST['caption']
        newpost = models.Post(user=this_user, content=content, caption=caption)
        newpost.save()

        return HttpResponseRedirect(reverse('instagmar_app:mainview'))

    else:
        form = forms.PostForm()
        return render(request, 'instagmar_app/newpost_page.html', context={"form": form})

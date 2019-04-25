from django.urls import path, re_path
from . import views

app_name = 'instagmar_app'

urlpatterns = [
    # path('', views.testview, name="testview"),
    path('', views.signupview, name="signupview"),
    path('home', views.homeview, name="homeview"),
    path('login', views.loginview, name="loginview"),
    path('logout', views.logoutview, name="logoutview"),
    path('posts', views.postsview, name='postsview')

]

from django.urls import path, re_path
from . import views

app_name = 'instagmar_app'

urlpatterns = [
    path('', views.signupview, name="signupview"),
    path('login', views.loginview, name="loginview")
]

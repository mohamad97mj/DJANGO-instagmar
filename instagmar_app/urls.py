from django.urls import path, re_path
from . import views

app_name = 'instagmar_app'

urlpatterns = [
    path('', views.loginview, name="login_view"),
]

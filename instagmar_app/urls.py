from django.urls import path, re_path
from . import views

app_name = 'instagmar_app'

urlpatterns = [
    # path('', views.testview, name="testview"),
    path('', views.signupview, name="signupview"),
    path('instagmar', views.mainview, name="mainview"),
    # path('base', views.baseview, name="baseview"),
    path('login', views.loginview, name="loginview"),
    path('logout', views.logoutview, name="logoutview"),
    path('posts', views.postsview, name='postsview'),
    path('newpost', views.newpostview, name="newpostview")
]

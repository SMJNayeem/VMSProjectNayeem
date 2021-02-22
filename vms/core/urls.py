from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice', views.notice, name='notice'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutUser, name='logoutPage'),
    path('register', views.registerPage, name='registerPage'),
]
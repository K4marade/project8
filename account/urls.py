from django.urls import path

from user_account import views

urlpatterns = [
    path('', views.login_account, nom="login_account"),
]
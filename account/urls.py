from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='account/login_old.html'), name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.profile_view, name="profile"),
    path('aliments/', views.aliments_view, name="aliments"),
]

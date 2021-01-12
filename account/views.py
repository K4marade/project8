from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Améliorer le register pour que le username switch sur le nouvel utilisateur créé. Voir ".cleaned_data" ?
def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'registration/register.html', locals())
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'registration/register.html', locals())


# def register_view(request):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Bonjour ' + user + ", vous pouvez maintenant vous connecter")
#             return redirect('login')
#
#     return render(request, 'registration/register.html', locals())


# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data.get('username')
#                 raw_password = form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=raw_password)
#                 login(request, user)
#                 return redirect('home')
#         else:
#             form = RegisterForm()
#         return render(request, 'registration/register.html', {'form': form})


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == "POST":
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Username OU Password incorrect')
#
#         return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


@login_required
def aliments_view(request):
    return render(request, 'account/aliments.html')

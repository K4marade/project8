from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'account/register.html', locals())
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Veuillez réessayer")
        else:
            form = RegisterForm()
            messages.error(request, 'Les informations renseignées ne sont pas valides')
        return render(request, 'account/register.html', locals())


def dashboard(request):
    return render(request, 'account/dashboard.html')

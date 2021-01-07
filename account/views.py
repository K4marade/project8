from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib.auth import logout


# Améliorer le register pour que le username switch sur le nouvel utilisateur créé. Voir ".cleaned_data" ?
def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'account/register.html', locals())
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def dashboard_view(request):
    return render(request, 'account/dashboard.html')

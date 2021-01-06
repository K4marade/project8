from django.shortcuts import render, redirect
from account.forms import RegisterForm


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'account/register.html', locals())
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


def dashboard(request):
    return render(request, 'account/dashboard.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib.auth import logout, login, authenticate


# Améliorer le register pour que le username switch sur le nouvel utilisateur créé. Voir ".cleaned_data" ?
# def register_view(request):
#     if request.method == "GET":
#         form = RegisterForm()
#         return render(request, 'account/register.html', locals())
#     elif request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


@login_required
def aliments_view(request):
    return render(request, 'account/aliments.html')

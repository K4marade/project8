from django.shortcuts import render
from django.views.generic.list import ListView


def home_view(request):
    return render(request, 'home.html')


def legal_view(request):
    return render(request, 'legal.html')

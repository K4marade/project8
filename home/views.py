from django.shortcuts import render
from products.models import Product


def home_view(request):
    return render(request, 'home.html')


def legal_view(request):
    return render(request, 'legal.html')


def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        product = Product.objects.all().filter(name=search)
        return render(request, 'search_product.html', {'product': product})
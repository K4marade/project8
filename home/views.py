from django.shortcuts import render
from django.views.generic.list import ListView


def home_view(request):
    return render(request, 'home.html')


def legal_view(request):
    return render(request, 'legal.html')


# def search_view(request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         product = Product.objects.filter(name__icontains=search).distinct('barcode')
#         return render(request, 'search_list.html', {'product': product})

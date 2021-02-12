from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, Http404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin
from products.models import Product, Category
from django.core.paginator import Paginator


def search_list_view(request):
    search = request.GET.get('search')

    if not search.strip():

        message = messages.info(
            request, "Merci de rentrer une recherche valide")
        return render(request, 'home.html', locals())

    elif search:
        # try:
        products = Product.objects.filter(name__icontains=search).distinct('categories')
        context = {
            "products": products,
        }

        return render(request, 'search_list.html', context)

        # except Product.DoesNotExist:
        # raise Http404("Le produit n'a pas été trouvé")
        # self.name = get_object_or_404(Product, name=self.kwargs['name'])
        # return self.request.GET.get(self.name)


def results_view(request, product_id):
    title = Product.objects.get(id=product_id).name
    image = Product.objects.get(id=product_id).small_image
    substitutes = Product.objects.filter(categories__products__id=product_id).order_by('nutriscore').exclude('')

    context = {
        "title": title,
        "image": image,
        "substitutes": substitutes

    }

    return render(request, 'results.html', context)

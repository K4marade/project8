from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Product, Favorite
from account.models import UserAuth
from django.db import IntegrityError


def search_list_view(request):
    """
    Function that displays the search list page with
    found aliments from user input search or
    redirects the user to home page if invalid input

     **Template:**
    :template:`home.html` and :template:`search_list.html`
    """

    search = request.GET.get('search')
    try:
        if not search.strip():
            message = messages.error(
                request, "Merci de rentrer une recherche valide")
            return render(request, 'home.html', locals())

        elif search:
            products = Product.objects.filter(name__icontains=search).order_by(
                'nutriscore').distinct()
            return render(request, 'search_list.html', locals())
    except AttributeError:
        return redirect('home')


def results_view(request, product_id):
    """
    Function that displays the results page with found substitutes

     **Template:**
    :template:`results.html`
    """

    prod_title = Product.objects.get(id=product_id).name
    prod_image = Product.objects.get(id=product_id).small_image
    substitutes = Product.objects.filter(
        categories__products__id=product_id).order_by(
        'nutriscore').exclude(id=product_id)
    return render(request, 'results.html', locals())


def save_product_view(request, product_id, substitute_id):
    """
    Function that stores saved aliment in favorite from user session,
    or display an error message if aliment already saved,
    or redirect to login if user is not authenticated

     **Template:**
    :template:`results.html` and :template:`login.html`
    """

    if request.user.is_authenticated:
        current_user = UserAuth.objects.get(
            id=request.session['_auth_user_id']
        )
        product = Product.objects.get(id=product_id).id
        substitute = Product.objects.get(id=substitute_id).id
        try:
            Favorite.objects.create(user_id=current_user,
                                    ali_source_id=product,
                                    ali_sub_id=substitute)
            messages.success(request, 'Le produit a bien été sauvegardé')
            return redirect('results', product)
        except IntegrityError:
            messages.error(request, 'Ce produit est déjà dans vos favoris')
            return redirect('results', product)
    else:
        messages.warning(request, "Connectez-vous pour sauvegarder un produit")
        return redirect('login')


def detail_view(request, product_id):
    """
    Fucntion that displays detail page for a product

     **Template:**
    :template:`detail.html`
    """

    product = Product.objects.get(id=product_id)
    return render(request, 'detail.html', locals())

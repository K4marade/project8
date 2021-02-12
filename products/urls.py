from django.urls import path
from products import views

urlpatterns = [
    path('search_list/', views.search_list_view, name='search'),
    path('results/', views.results_view, name='results'),
    path('results/<int:product_id>/', views.results_view, name='results'),
    # path('search_product/', views.search_view, name='search'),
]

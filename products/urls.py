from django.urls import path
from products import views

urlpatterns = [
    path('search_list/', views.search_list_view, name='search'),
    path('results/', views.results_view, name='results'),
    path('results/<int:product_id>/', views.results_view, name='results'),
    path('save/', views.save_product_view, name='save'),
    path('save/<int:product_id>/<int:substitute_id>',
         views.save_product_view, name='save'),
    path('detail', views.detail_view, name='detail'),
    path('detail/<int:product_id>', views.detail_view, name='detail'),
]

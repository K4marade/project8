from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import TestCase, Client

from products.models import Product
from products.views import search_list_view
import pytest


@pytest.mark.django_db
class TestViews(TestCase):  # (TestCase)

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.c = Client()
        # mixer.blend(Product)
        # cls.factory = RequestFactory()

    def test_search_list_view(self):
        response_with_input = self.c.get('/products/search_list/', {'search': "nutella"})
        response_without_input = self.c.get('/products/search_list/', {'search': ""})
        # response = self.c.get(reverse('search'))

        assert response_with_input.status_code == 200
        assert response_with_input.context['search'] == "nutella"
        assert response_without_input.status_code == 200

    # def test_results_view(self):
    #     mixer.blend(Product, id=75, name="Nutella")
    #     result_url = reverse('results', kwargs={'id': 75})
    #     response = self.c.get('/products/results/75')
    #     assert response.status_code == 200

from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import TestCase, Client

from products.models import Product, Category
from products.views import search_list_view
import pytest


@pytest.mark.django_db
class TestViews(TestCase):  # (TestCase)

    def setUp(self) -> None:
        self.user = get_user_model()
        self.c = Client()
        mixer.blend(Product)
        mixer.blend(Category)
        # cls.factory = RequestFactory()

    def test_search_list_view(self):
        response_with_input = self.c.get("/products/search_list/", {"search": "nutella"})
        response_without_input = self.c.get("/products/search_list/", {"search": ""})
        # response = self.c.get(reverse("search"))

        assert response_with_input.status_code == 200
        assert response_with_input.context["search"] == "nutella"
        assert response_without_input.status_code == 200

    def test_results_view(self):
        results_url = reverse("results", kwargs={"product_id": 1})
        response = self.c.get(results_url)
        assert response.status_code == 200

    def test_save_product_view(self):
        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")
        self.c.login(username="Leonard", password="12345Testing")
        save_url = reverse("save", kwargs={"product_id": 1, "substitute_id": 2})
        response = self.c.get(save_url)
        assert response.status_code == 200
from django.contrib.auth import get_user_model
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import TestCase, Client

from products.models import Product, Favorite
import pytest


class TestViews(TestCase):

    @pytest.mark.django_db
    def setUp(self) -> None:
        self.user = get_user_model()
        self.c = Client()
        self.product = mixer.blend(Product, id=1)
        self.substitute = mixer.blend(Product, id=2)

    def test_search_list_view(self):
        response_with_input = self.c.get("/products/search_list/", {"search": "nutella"})
        response_without_input = self.c.get("/products/search_list/", {"search": ""})

        assert response_with_input.status_code == 200
        assert response_with_input.context["search"] == "nutella"
        assert response_without_input.status_code == 200

    @pytest.mark.django_db
    def test_results_view(self):
        results_url = reverse("results", kwargs={"product_id": 1})
        response = self.c.get(results_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authenticated_save_product_view(self):
        self.user.objects.create_user(username="test_username",
                                      email="test_email@test.com",
                                      password="test_password!")
        self.c.login(username="test_username", password="test_password!")

        # Assert no products are saved yet in database
        assert Favorite.objects.count() == 0

        save_url = reverse("save", kwargs={"product_id": 1, "substitute_id": 2})
        response = self.c.get(save_url)

        # Assert user stays on the results page when a product is saved
        assert response.status_code == 302
        assert response.url == reverse("results", kwargs={"product_id": 1})
        # Assert one product is now saved in database
        assert Favorite.objects.count() == 1

    # @pytest.mark.django_db
    # def test_save_product_already_in_favorite(self):
    #     self.user.objects.create_user(username="test_username",
    #                                   email="test_email@test.com",
    #                                   password="test_password!")
    #     self.c.login(username="test_username", password="test_password!")
    #     user_id = self.c.session.get('_auth_user_id')
    #     mixer.blend(Favorite, user_id=user_id, ali_source_id=1, ali_sub_id=2)
    #
    #     assert Favorite.objects.count() == 1

    @pytest.mark.django_db
    def test_unauthenticated_save_product_view(self):
        save_url = reverse("save", kwargs={"product_id": 1, "substitute_id": 2})
        response = self.c.get(save_url)

        # Assert user is redirected to login page
        assert response.status_code == 302
        assert response.url == reverse('login')

    def test_detail_view(self):
        detail_url = reverse("detail", kwargs={"product_id": 1})
        response = self.c.get(detail_url)

        assert response.status_code == 200

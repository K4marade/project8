from django.test import TestCase, Client
from django.urls import reverse
from home.views import *


class TestViews(TestCase):

    def setUp(self) -> None:
        self.c = Client()

    def test_home_view(self):
        home_url = reverse('home')
        response = self.c.get(home_url)

        assert response.status_code == 200

    def test_legal_view(self):
        legal_url = reverse('legal')
        response = self.c.get(legal_url)

        assert response.status_code == 200

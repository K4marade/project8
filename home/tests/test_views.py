from django.test import RequestFactory, TestCase
from django.urls import reverse
from home.views import *


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.factory = RequestFactory()

    def test_home_view(self):
        path = reverse('home')
        request = self.factory.get(path)

        response = home_view(request)
        assert response.status_code == 200

    def test_legal_view(self):
        path = reverse('legal')
        request = RequestFactory().get(path)

        response = legal_view(request)
        assert response.status_code == 200

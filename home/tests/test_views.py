from django.test import RequestFactory
from django.urls import reverse
from home.views import *


class TestViews:

    def test_home_view(self):
        path = reverse('home')
        request = RequestFactory().get(path)

        response = home_view(request)
        assert response.status_code == 200

    def test_legal_view(self):
        path = reverse('legal')
        request = RequestFactory().get(path)

        response = legal_view(request)
        assert response.status_code == 200

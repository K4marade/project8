from django.urls import reverse
from django.contrib.auth import get_user_model
from account.models import UserAuth
import pytest


class TestViews:

    @staticmethod
    @pytest.mark.parametrize('param', [
        'register',
        'login',
        'home',
        'profile',
        'favorite'
    ])
    def test_render_views(client, param):
        temp_url = reverse(param)
        response = client.get(temp_url)
        assert response.status_code in (200, 302)  # 302 is redirection status code

    # @pytest.mark.django_db
    # def test_user_register(self, client, user_data):
    #     user_model = get_user_model()
    #     assert user_model.objects.count() == 0
    #     register_url = reverse('register')
    #     response = client.post(register_url, user_data)
    #     # assert user_model.objects.count() == 1
    #     assert response.status_code == 200
    #     # assert response.url == reverse('home')

    @pytest.mark.django_db
    def test_user_login(self, client, create_test_user, user_data):
        user_model = get_user_model()
        assert user_model.objects.count() == 1
        login_url = reverse('login')
        response = client.post(login_url, data=user_data)
        assert response.status_code == 302
        assert response.url == reverse('home')

    @pytest.mark.django_db
    def test_user_logout(self, client, authenticated_user):
        logout_url = reverse('logout')
        response = client.get(logout_url)
        assert response.status_code == 302
        assert response.url == reverse('home')

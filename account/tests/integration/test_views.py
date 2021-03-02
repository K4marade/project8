from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
import pytest


class TestViews(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model()
        self.c = Client()


    def test_register_view(self):
        # Assert no user is registered yet
        assert self.user.objects.count() == 0
        register_url = reverse('register')
        assert self.c.get(register_url).status_code == 200
        response = self.c.post(register_url, {
            "username": "Leonard",
            "email": "leo@leo.com",
            "password1": "12345Testing",
            "password2": "12345Testing"
        })

        # Assert one user is now registered
        assert self.user.objects.count() == 1

        # Homepage redirection once registered
        assert response.status_code == 302
        assert response.url == reverse('home')

    def test_user_login_view(self):
        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")
        assert self.user.objects.count() == 1
        login_url = reverse("login")
        assert self.c.get(login_url).status_code == 200

        # Correct username and password:
        response = self.c.post(login_url, {"username": "Leonard",
                                           "password": "12345Testing"})

        # Homepage redirection once logged in
        assert response.status_code == 302
        assert response.url == reverse("home")

        # Incorrect password:
        response_with_wrong_password = self.c.post(login_url, {"username": "Leonard",
                                                               "password": "wrong_password"})
        assert response_with_wrong_password.status_code == 200
        assert b"Your username and password didn\'t match" in response_with_wrong_password.content

    def test_logout_view(self):
        logout_url = reverse("logout")
        response = self.c.get(logout_url)

        # Homepage redirection once logged out
        assert response.status_code == 302
        assert response.url == reverse("home")

    def test_profile_view(self):
        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")
        profile_url = reverse("profile")
        response = self.c.get(profile_url)
        assert response.status_code == 200

    def test_favorite_view(self):
        self.user.objects.create_user(username="Leonard",
                                      email="leo@leo.com",
                                      password="12345Testing")

        self.c.login(username="Leonard", password="12345Testing")
        favorite_url = reverse("favorite")
        response = self.c.get(favorite_url)
        assert response.status_code == 200

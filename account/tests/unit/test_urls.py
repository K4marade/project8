from django.urls import reverse, resolve


class TestUrls:
    """Class that tests account urls"""

    def test_login_url(self):
        """Tests login url"""

        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_register_url(self):
        """Tests register url"""

        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_logout_url(self):
        """Tests logout url"""

        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_profile_url(self):
        """Tests profile url"""

        path = reverse('profile')
        assert resolve(path).view_name == 'profile'

    def test_favorite_url(self):
        """Tests favorite url"""

        path = reverse('favorite')
        assert resolve(path).view_name == 'favorite'

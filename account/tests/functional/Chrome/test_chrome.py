from django.test import Client
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1200")


class ChromeFunctionalTestCase(StaticLiveServerTestCase):
    """Class that defines Chrome functional tests"""

    def setUp(self):
        """Tests setup method"""

        self.driver = webdriver.Chrome(options=chrome_options, )
        self.driver.maximize_window()
        self.user = get_user_model()
        self.client = Client()

    def tearDown(self):
        """Tests tear down method"""

        self.driver.close()

    def get_element(self, selector):
        """Method that uses a css selector to return
        an element from the driver."""

        return self.driver.find_element_by_css_selector(selector)

    def test_user_can_connect_and_disconnect(self):
        """
        Test user is on the homepage and :
            - clicks on the login button
            - inputs its connexion info and clicks on "connexion" button
            - clicks on the logout button from the homepage and is disconnected
        """

        self.user.objects.create_user(
            username="LeonardCOLIN", password="1234Testing!"
        )

        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the login button
        self.get_element("#button-login").click()

        time.sleep(1)

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse(
            'login') + "?next=/"

        self.get_element("#id_username").send_keys("LeonardCOLIN")
        self.get_element("#id_password").send_keys("1234Testing!")
        self.get_element("#button-connexion").click()

        time.sleep(3)

        # Assert the current url is the home url
        assert self.driver.current_url == self.live_server_url + \
               reverse("home")
        # Assert the profile link is available once user is authenticated
        assert "button-profile" in self.driver.page_source

        # User clicks on the logout button
        self.get_element("#button-logout").click()
        time.sleep(1)
        # Assert user is logged out
        assert "Vous êtes bien déconnecté" in self.driver.page_source

    def test_user_can_register(self):
        """
        Test user is on the homepage and:
            - clicks on the register button
            - inputs its username, email and password
            - clicks on the "validate" button and is now registered
        """

        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the register button
        self.get_element("#button-register").click()

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse(
            'register') + "?next=/"
        time.sleep(2)

        self.get_element("#id_username").send_keys("Leonard")
        self.get_element("#id_email").send_keys("leocolin@leo.com")
        self.get_element("#id_password1").send_keys("testPassword1234")
        self.get_element("#id_password2").send_keys("testPassword1234")
        time.sleep(2)
        self.get_element("#button-validate").click()
        time.sleep(1)
        assert "Bienvenue Leonard" in self.driver.page_source

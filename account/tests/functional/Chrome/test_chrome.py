from django.shortcuts import redirect
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import selenium.webdriver.support.ui as ui

chrome_options = webdriver.ChromeOptions()


# chrome_options.add_argument("--headless")


class ChromeFunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # (options=chrome_options)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.wait = ui.WebDriverWait(self.driver, 30)

    def tearDown(self):
        self.driver.close()

    def get_element(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def test_user_can_connect_and_disconnect(self):
        user = get_user_model()
        user.objects.create_user(
            username="LeonardCOLIN", password="1234Testing!"
        )
        self.driver.get(self.live_server_url)

        # User is on the homepage and clicks on the login button
        self.get_element("#button-login").click()

        # Assert the current url is the login url
        assert self.driver.current_url == self.live_server_url + reverse('login') + "?next=/"

        username = self.driver.find_element_by_id("id_username")
        username.click()
        self.driver.implicitly_wait(2)
        username.send_keys("LeonardCOLIN")

        password = self.driver.find_element_by_id("id_password")
        password.click()
        password.send_keys("1234Testing!")
        self.driver.find_element_by_id("button-connexion").click()
        self.wait.until(lambda driver: self.driver.find_element_by_id("button-profile").is_displayed())
        assert self.driver.current_url == self.live_server_url + reverse("home")

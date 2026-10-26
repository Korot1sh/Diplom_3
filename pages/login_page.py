import allure

from locators import login_locators as L
from utils.constants import LOGIN_PATH

from .base_page import BasePage


class LoginPage(BasePage):
    URL = LOGIN_PATH

    @allure.step("Открыть страницу входа")
    def open_login(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Перейти к восстановлению пароля")
    def open_password_recovery(self):
        self.click(L.FORGOT_PASSWORD_LINK)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.wait_visible(L.EMAIL).send_keys(email)
        self.wait_visible(L.PASSWORD).send_keys(password)
        self.click(L.LOGIN_BUTTON)

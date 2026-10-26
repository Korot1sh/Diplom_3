import allure

from locators import reset_password_locators as L
from utils.constants import RESET_PASSWORD_PATH

from .base_page import BasePage


class ResetPasswordPage(BasePage):
    URL = RESET_PASSWORD_PATH

    @allure.step("Открыть страницу установки нового пароля")
    def open_page(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Нажать показать/скрыть пароль")
    def toggle_password(self):
        self.click(L.SHOW_PASSWORD_BUTTON)

    @allure.step("Получить класс поля пароля")
    def password_field_class(self):
        return self.wait_visible(L.PASSWORD).get_attribute("class")

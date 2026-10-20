import allure
from .base_page import BasePage
from locators import reset_password_locators as L


class ResetPasswordPage(BasePage):
    URL = "/reset-password"

    @allure.step("Открыть страницу установки нового пароля")
    def open_page(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Нажать показать/скрыть пароль")
    def toggle_password(self):
        self.click(L.SHOW_PASSWORD_BUTTON)

    @allure.step("Получить класс поля пароля")
    def password_field_class(self):
        return self.wait_visible(L.PASSWORD).get_attribute("class")

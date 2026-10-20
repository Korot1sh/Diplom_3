import allure
from .base_page import BasePage
from locators import forgot_password_locators as L


class ForgotPasswordPage(BasePage):
    URL = "/forgot-password"

    @allure.step("Открыть страницу восстановления пароля")
    def open_page(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Ввести email для восстановления")
    def enter_email(self, email):
        field = self.wait_visible(L.EMAIL)
        field.clear()
        field.send_keys(email)

    @allure.step("Нажать «Восстановить»")
    def recover(self):
        self.click(L.RECOVER_BUTTON)

    @allure.step("Показать/скрыть пароль")
    def toggle_password(self):
        self.click(L.SHOW_PASSWORD_BUTTON)

    @allure.step("Получить CSS-свойство поля пароля")
    def password_field_outline(self):
        return self.wait_visible(L.PASSWORD_INPUT).value_of_css_property("outline")

    @allure.step("Получить класс поля пароля")
    def password_field_class(self):
        return self.wait_visible(L.PASSWORD_INPUT).get_attribute("class")

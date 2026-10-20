import allure
from .base_page import BasePage
from locators import account_locators as L


class AccountPage(BasePage):
    URL = "/account"

    @allure.step("Открыть личный кабинет")
    def open_account(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Перейти в историю заказов")
    def open_history(self):
        self.click(L.HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(L.LOGOUT_BUTTON)

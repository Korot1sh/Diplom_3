import allure

from locators import account_locators as L
from utils.constants import ACCOUNT_PATH

from .base_page import BasePage


class AccountPage(BasePage):
    URL = ACCOUNT_PATH

    @allure.step("Открыть личный кабинет")
    def open_account(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Перейти в историю заказов")
    def open_history(self):
        self.click(L.HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(L.LOGOUT_BUTTON)

import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from utils.constants import ACCOUNT_PATH, LOGIN_PATH, ORDER_HISTORY_PATH


@allure.epic("Stellar Burgers")
@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_account(self, driver, base_url, auth_context):
        page = AccountPage(driver)
        page.open_account(base_url)
        assert page.url_contains(ACCOUNT_PATH)

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, base_url, auth_context):
        page = AccountPage(driver)
        page.open_account(base_url)
        page.open_history()
        assert page.url_contains(ORDER_HISTORY_PATH)

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, base_url, auth_context):
        page = AccountPage(driver)
        page.open_account(base_url)
        page.logout()
        assert LoginPage(driver).url_contains(LOGIN_PATH)

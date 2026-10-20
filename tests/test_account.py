import allure
from pages.constructor_page import ConstructorPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage


@allure.epic("Stellar Burgers")
@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_account(self, driver, base_url, auth_context):
        AccountPage(driver).open_account(base_url)
        assert "/account" in driver.current_url

    @allure.title("Переход в историю заказов")
    def test_open_order_history(self, driver, base_url, auth_context):
        page = AccountPage(driver)
        page.open_account(base_url)
        page.open_history()
        page.url_contains("/account/order-history")

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, base_url, auth_context):
        page = AccountPage(driver)
        page.open_account(base_url)
        page.logout()
        LoginPage(driver).url_contains("/login")

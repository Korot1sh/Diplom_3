import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет")
    def test_open_personal_account(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        MainPage(driver).open_account()
        assert "/account" in driver.current_url

    @allure.title("Открытие истории заказов")
    def test_open_order_history(self, driver, logged_in):
        MainPage(driver).open_account()
        ProfilePage(driver).open_order_history()
        assert "orders" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, logged_in):
        MainPage(driver).open_account()
        ProfilePage(driver).logout()
        assert "/login" in driver.current_url or "Войти" in driver.page_source

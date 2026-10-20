import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.epic("Stellar Burgers")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на восстановление пароля из формы входа")
    @allure.story("Навигация")
    def test_open_password_recovery(self, driver, base_url):
        login = LoginPage(driver)
        login.open_login(base_url)
        login.open_password_recovery()
        ForgotPasswordPage(driver).url_contains("/forgot-password")

    @allure.title("Ввод email и отправка запроса на восстановление")
    @allure.story("Восстановление пароля")
    def test_submit_password_recovery(self, driver, base_url, user):
        page = ForgotPasswordPage(driver)
        page.open_page(base_url)
        page.enter_email(user["data"]["email"])
        page.recover()
        ResetPasswordPage(driver).url_contains("/reset-password")

    @allure.title("Клик по показать/скрыть пароль активирует поле пароля")
    @allure.story("Восстановление пароля")
    def test_password_toggle_activates_field(self, driver, base_url):
        page = ResetPasswordPage(driver)
        page.open_page(base_url)
        before = page.password_field_class()
        page.toggle_password()
        after = page.password_field_class()
        assert after != before

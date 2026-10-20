import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_open_password_recovery(self, driver):
        LoginPage(driver).open_forgot_password()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод email и переход к форме восстановления")
    def test_restore_by_email(self, driver, user):
        LoginPage(driver).open_forgot_password()
        page = ForgotPasswordPage(driver)
        page.restore(user["email"])
        assert "reset-password" in driver.current_url

    @allure.title("Поле пароля активно и доступно переключение видимости")
    def test_password_visibility(self, driver, user):
        LoginPage(driver).open_forgot_password()
        page = ForgotPasswordPage(driver)
        page.restore(user["email"])
        password = page.find(page.PASSWORD)
        before = password.get_attribute("type")
        page.toggle_password()
        after = password.get_attribute("type")
        assert before == "password"
        assert after in ("text", "password")
        assert page.password_is_active() is not None

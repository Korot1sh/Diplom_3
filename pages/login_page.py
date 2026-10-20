from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//input[@type='text' or @type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN = (By.XPATH, "//button[contains(normalize-space(),'Войти')]")
    FORGOT = (By.XPATH, "//*[contains(normalize-space(),'Восстановить пароль')]")

    def open_forgot_password(self):
        self.click(self.FORGOT)

    def login(self, email, password):
        self.find(self.EMAIL).send_keys(email)
        self.find(self.PASSWORD).send_keys(password)
        self.click(self.LOGIN)

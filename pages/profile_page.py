from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProfilePage(BasePage):
    ORDER_HISTORY = (By.XPATH, "//*[contains(normalize-space(),'История заказов')]")
    LOGOUT = (By.XPATH, "//*[normalize-space()='Выход']")

    def open_order_history(self):
        self.click(self.ORDER_HISTORY)

    def logout(self):
        self.click(self.LOGOUT)

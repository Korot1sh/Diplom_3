from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderFeedPage(BasePage):
    ALL_TIME = (By.XPATH, "//*[contains(normalize-space(),'Выполнено за всё время')]")
    TODAY = (By.XPATH, "//*[contains(normalize-space(),'Выполнено за сегодня')]")
    IN_PROGRESS = (By.XPATH, "//*[contains(normalize-space(),'В работе')]")
    ORDERS = (By.XPATH, "//*[contains(@class,'OrderHistory') or contains(@class,'OrderList') or contains(@class,'Order')]//li")
    MODAL = (By.XPATH, "//div[contains(@class,'modal')]")

    def all_time_value(self):
        return self._near_value(self.ALL_TIME)

    def today_value(self):
        return self._near_value(self.TODAY)

    def in_progress_text(self):
        return self.text(self.IN_PROGRESS)

    def open_first_order(self):
        self.click((By.XPATH, "(//*[contains(@class,'Order') and .//*[contains(@class,'text')]])[1]"))

    def open_order_by_number(self, number):
        self.click((By.XPATH, f"//*[contains(normalize-space(),'{number}')]/ancestor::*[.//button or self::li or self::div][1]"))

    def _near_value(self, label):
        node = self.find(label)
        parent = node.find_element(By.XPATH, "..")
        text = parent.text
        return text

import allure

from locators import feed_locators as L
from utils.constants import FEED_PATH

from .base_page import BasePage


class FeedPage(BasePage):
    URL = FEED_PATH

    @allure.step("Открыть ленту заказов")
    def open_feed(self, base_url):
        self.open(base_url + self.URL)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def total_all(self):
        return int(self.text(L.TOTAL_ALL).replace(" ", "").strip())

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def total_today(self):
        return int(self.text(L.TOTAL_TODAY).replace(" ", "").strip())

    @allure.step("Дождаться увеличения «Выполнено за всё время»")
    def wait_total_all_increased(self, previous):
        self.wait.until(lambda _: self.total_all() >= previous + 1)

    @allure.step("Дождаться увеличения «Выполнено за сегодня»")
    def wait_total_today_increased(self, previous):
        self.wait.until(lambda _: self.total_today() >= previous + 1)

    @allure.step("Открыть заказ по номеру {number}")
    def open_order_by_number(self, number):
        locator = ("xpath", f"//*[contains(normalize-space(), '{number}')]")
        self.click(locator)

    @allure.step("Получить номер заказа из модального окна")
    def modal_order_number(self):
        text = self.text(L.MODAL_ORDER_NUMBER)
        return "".join(ch for ch in text if ch.isdigit())

    @allure.step("Закрыть модальное окно заказа")
    def close_modal(self):
        self.click(L.MODAL_CLOSE)
        self.wait_modal_closed(L.MODAL)

    @allure.step("Дождаться номера заказа в ленте")
    def order_present(self, number):
        locator = ("xpath", f"//*[contains(normalize-space(), '{number}')]")
        self.wait_visible(locator)
        return True

    @allure.step("Дождаться номера заказа в блоке «В работе»")
    def order_present_in_progress(self, number):
        locator = (
            "xpath",
            f"//*[contains(normalize-space(), 'В работе') and "
            f".//*[contains(normalize-space(), '{number}')]]",
        )
        self.wait_visible(locator)
        return True

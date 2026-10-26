import allure

from locators import constructor_locators as L
from utils.constants import CONSTRUCTOR_PATH

from .base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step("Перейти в конструктор")
    def open_constructor(self):
        self.click(L.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def open_feed(self):
        self.click(L.FEED_LINK)

    def _ingredient(self, name):
        locator = (L.INGREDIENT_CARD[0], L.INGREDIENT_CARD[1].format(name=name))
        return self.find(locator)

    @allure.step("Открыть детали ингредиента {name}")
    def open_ingredient(self, name):
        card = self._ingredient(name)
        self.scroll_into_view(card)
        card.click()

    @allure.step("Получить название ингредиента в модальном окне")
    def modal_title(self):
        return self.text(L.MODAL_TITLE)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click(L.MODAL_CLOSE)
        self.wait_modal_closed(L.MODAL)

    @allure.step("Проверить, что модальное окно закрыто")
    def modal_is_closed(self):
        return not self.has_elements(L.MODAL)

    @allure.step("Получить каунтер ингредиента {name}")
    def ingredient_counter(self, name):
        card = self._ingredient(name)
        counters = card.find_elements(*L.INGREDIENT_COUNTER)
        return int(counters[0].text) if counters and counters[0].text else 0

    @allure.step("Добавить ингредиент {name} в заказ")
    def add_ingredient(self, name):
        source = self._ingredient(name)
        target = self.wait_visible(L.CONSTRUCTOR_AREA)
        self.scroll_into_view(source)
        self.scroll_into_view(target)
        self.drag_and_drop(source, target)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(L.ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def order_number(self):
        text = self.text(L.ORDER_MODAL_NUMBER)
        return "".join(ch for ch in text if ch.isdigit())

    @allure.step("Открыть конструктор по URL")
    def open_constructor_page(self, base_url):
        self.open(base_url + CONSTRUCTOR_PATH)

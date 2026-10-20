import allure
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from locators import constructor_locators as L


class ConstructorPage(BasePage):
    @allure.step("Перейти в конструктор")
    def open_constructor(self):
        self.click(L.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def open_feed(self):
        self.click(L.FEED_LINK)

    def _ingredient(self, name):
        return self.driver.find_element(
            L.INGREDIENT_CARD[0], L.INGREDIENT_CARD[1].format(name=name)
        )

    @allure.step("Открыть детали ингредиента {name}")
    def open_ingredient(self, name):
        card = self._ingredient(name)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card)
        card.click()

    @allure.step("Получить название ингредиента в модальном окне")
    def modal_title(self):
        return self.text(L.MODAL_TITLE)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click(L.MODAL_CLOSE)
        self.wait_modal_closed(L.MODAL)

    @allure.step("Получить каунтер ингредиента {name}")
    def ingredient_counter(self, name):
        card = self._ingredient(name)
        try:
            return int(card.find_element(*L.INGREDIENT_COUNTER).text)
        except Exception:
            return 0

    @allure.step("Добавить ингредиент {name} в заказ")
    def add_ingredient(self, name):
        source = self._ingredient(name)
        target = self.wait_visible(L.CONSTRUCTOR_AREA)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(L.ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def order_number(self):
        text = self.text(L.ORDER_MODAL_NUMBER)
        digits = "".join(ch for ch in text if ch.isdigit())
        return digits

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR = (By.XPATH, "//*[normalize-space()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//*[contains(normalize-space(),'Лента заказов')]")
    ACCOUNT = (By.XPATH, "//*[contains(normalize-space(),'Личный кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(normalize-space(),'Оформить заказ')]")
    MODAL = (By.XPATH, "//div[contains(@class,'modal')]")
    MODAL_CLOSE = (By.XPATH, "//div[contains(@class,'modal')]//button")
    INGREDIENTS = (By.XPATH, "//*[contains(@class,'BurgerIngredient')]")
    BUNS = (By.XPATH, "//*[contains(normalize-space(),'булка')]")
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//*[contains(@class,'BurgerConstructor') or contains(@class,'constructor')]")

    def open_constructor(self):
        self.click(self.CONSTRUCTOR)

    def open_order_feed(self):
        self.click(self.ORDER_FEED)

    def open_account(self):
        self.click(self.ACCOUNT)

    def close_popup(self):
        self.click(self.MODAL_CLOSE)

    def ingredient_card(self, name=None):
        if name:
            return self.find((By.XPATH, f"//*[contains(normalize-space(),{self._xpath_literal(name)})]/ancestor::*[.//button][1]"))
        return self.find((By.XPATH, "(//*[contains(@class,'BurgerIngredient')])[1]"))

    @staticmethod
    def _xpath_literal(value):
        if "'" not in value:
            return f"'{value}'"
        parts = value.split("'")
        return "concat(" + ", \"'\", ".join(f"'{p}'" for p in parts) + ")"

    def open_ingredient(self, name=None):
        card = self.ingredient_card(name)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card)
        card.click()

    def drag_ingredient_to_constructor(self, name=None):
        source = self.ingredient_card(name)
        target = self.find(self.CONSTRUCTOR_DROP_ZONE)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)
        ActionChains(self.driver).move_to_element(source).click_and_hold().move_to_element(target).release().perform()

    def ingredient_counter(self, name=None):
        card = self.ingredient_card(name)
        try:
            return card.find_element(By.XPATH, ".//*[contains(@class,'counter')]").text
        except Exception:
            return ""

    def create_order(self):
        self.click(self.ORDER_BUTTON)

import re
import allure

from pages.main_page import MainPage


@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Открытие конструктора")
    def test_constructor_is_available(self, driver):
        page = MainPage(driver)
        page.open_constructor()
        assert "Конструктор" in driver.page_source

    @allure.title("Открытие деталей ингредиента и закрытие popup")
    def test_ingredient_details_popup(self, driver):
        page = MainPage(driver)
        page.open_ingredient()
        assert page.find(page.MODAL).is_displayed()
        page.close_popup()
        assert not driver.find_elements(*page.MODAL)

    @allure.title("При добавлении ингредиента увеличивается его счётчик")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        before_text = page.ingredient_counter()
        before = int(re.search(r"\d+", before_text).group()) if re.search(r"\d+", before_text) else 0
        page.drag_ingredient_to_constructor()
        after_text = page.ingredient_counter()
        after = int(re.search(r"\d+", after_text).group()) if re.search(r"\d+", after_text) else 0
        assert after > before

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, driver, logged_in):
        page = MainPage(driver)
        page.drag_ingredient_to_constructor()
        page.create_order()
        assert page.find(page.MODAL).is_displayed()
        assert re.search(r"\d{4,}", page.find(page.MODAL).text)

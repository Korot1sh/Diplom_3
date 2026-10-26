import allure

from pages.constructor_page import ConstructorPage
from utils.constants import CONSTRUCTOR_PATH, FEED_PATH


@allure.epic("Stellar Burgers")
@allure.feature("Основной функционал")
class TestConstructor:

    @allure.title("Переход в конструктор")
    def test_open_constructor(self, driver, base_url):
        page = ConstructorPage(driver)
        page.open(base_url + FEED_PATH)
        page.open_constructor()
        assert page.url_is(base_url + CONSTRUCTOR_PATH)

    @allure.title("Переход в ленту заказов")
    def test_open_feed(self, driver, base_url):
        page = ConstructorPage(driver)
        page.open_constructor_page(base_url)
        page.open_feed()
        assert page.url_contains(FEED_PATH)

    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver, base_url):
        page = ConstructorPage(driver)
        page.open_constructor_page(base_url)
        page.open_ingredient("Флюоресцентная булка R2-D3")
        assert "Флюоресцентная булка R2-D3" in page.modal_title()

    @allure.title("Закрытие деталей ингредиента крестиком")
    def test_close_ingredient_details(self, driver, base_url):
        page = ConstructorPage(driver)
        page.open_constructor_page(base_url)
        page.open_ingredient("Флюоресцентная булка R2-D3")
        page.close_modal()
        assert page.modal_is_closed()

    @allure.title("Каунтер ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver, base_url):
        page = ConstructorPage(driver)
        page.open_constructor_page(base_url)
        ingredient = "Соус Spicy-X"
        before = page.ingredient_counter(ingredient)
        page.add_ingredient(ingredient)
        after = page.ingredient_counter(ingredient)
        assert after == before + 1

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, base_url, auth_context):
        page = ConstructorPage(driver)
        page.open_constructor_page(base_url)
        page.add_ingredient("Флюоресцентная булка R2-D3")
        page.add_ingredient("Соус Spicy-X")
        page.place_order()
        number = page.order_number()
        assert number.isdigit() and len(number) > 0

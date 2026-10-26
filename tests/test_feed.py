import allure

from pages.feed_page import FeedPage


@allure.epic("Stellar Burgers")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие деталей заказа в ленте")
    def test_open_order_details(self, driver, base_url, api, user, order_ingredients):
        ids, _, _ = order_ingredients
        created = api.create_order(user["token"], ids)
        number = str(created["order"]["number"])
        page = FeedPage(driver)
        page.open_feed(base_url)
        page.open_order_by_number(number)
        assert page.modal_order_number().endswith(number)

    @allure.title("Заказ пользователя из истории отображается в ленте")
    def test_user_order_is_visible_in_feed(self, driver, base_url, api, user, order_ingredients):
        ids, _, _ = order_ingredients
        created = api.create_order(user["token"], ids)
        number = str(created["order"]["number"])
        page = FeedPage(driver)
        page.open_feed(base_url)
        assert page.order_present(number)

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после заказа")
    def test_total_all_increases(self, driver, base_url, api, user, order_ingredients):
        ids, _, _ = order_ingredients
        page = FeedPage(driver)
        page.open_feed(base_url)
        before = page.total_all()
        created = api.create_order(user["token"], ids)
        page.refresh()
        page.wait_total_all_increased(before)
        assert page.total_all() >= before + 1

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после заказа")
    def test_total_today_increases(self, driver, base_url, api, user, order_ingredients):
        ids, _, _ = order_ingredients
        page = FeedPage(driver)
        page.open_feed(base_url)
        before = page.total_today()
        created = api.create_order(user["token"], ids)
        page.refresh()
        page.wait_total_today_increased(before)
        assert page.total_today() >= before + 1

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_appears_in_progress(self, driver, base_url, api, user, order_ingredients):
        ids, _, _ = order_ingredients
        page = FeedPage(driver)
        page.open_feed(base_url)
        created = api.create_order(user["token"], ids)
        number = str(created["order"]["number"])
        page.refresh()
        assert page.order_present_in_progress(number)

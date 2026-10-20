import re
import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


def order_number_from_modal(page):
    text = page.find(page.MODAL).text
    numbers = re.findall(r"\d{4,}", text)
    assert numbers, f"Номер заказа не найден в popup: {text}"
    return numbers[-1]


@allure.feature("Лента заказов")
class TestOrderFeed:
    def create_order(self, driver):
        page = MainPage(driver)
        page.drag_ingredient_to_constructor()
        page.create_order()
        number = order_number_from_modal(page)
        page.close_popup()
        return number

    @allure.title("Открытие деталей заказа в ленте")
    def test_open_order_details(self, driver):
        feed = OrderFeedPage(driver)
        MainPage(driver).open_order_feed()
        feed.open_first_order()
        assert feed.find(feed.MODAL).is_displayed()

    @allure.title("Заказ пользователя из истории отображается в ленте")
    def test_user_order_appears_in_feed(self, driver, logged_in):
        number = self.create_order(driver)
        MainPage(driver).open_order_feed()
        OrderFeedPage(driver).open_order_by_number(number)
        assert number in driver.page_source

    @allure.title("Счётчик выполненных заказов за всё время увеличивается")
    def test_all_time_counter_increases(self, driver, logged_in):
        MainPage(driver).open_order_feed()
        feed = OrderFeedPage(driver)
        before_text = feed.all_time_value()
        before = int(re.search(r"\d+", before_text).group())
        MainPage(driver).open_constructor()
        self.create_order(driver)
        MainPage(driver).open_order_feed()
        after_text = OrderFeedPage(driver).all_time_value()
        after = int(re.search(r"\d+", after_text).group())
        assert after > before

    @allure.title("Счётчик выполненных за сегодня заказов увеличивается")
    def test_today_counter_increases(self, driver, logged_in):
        MainPage(driver).open_order_feed()
        feed = OrderFeedPage(driver)
        before_text = feed.today_value()
        before = int(re.search(r"\d+", before_text).group())
        MainPage(driver).open_constructor()
        self.create_order(driver)
        MainPage(driver).open_order_feed()
        after_text = OrderFeedPage(driver).today_value()
        after = int(re.search(r"\d+", after_text).group())
        assert after > before

    @allure.title("Номер нового заказа отображается в разделе 'В работе'")
    def test_new_order_in_progress(self, driver, logged_in):
        number = self.create_order(driver)
        MainPage(driver).open_order_feed()
        assert number in OrderFeedPage(driver).in_progress_text()

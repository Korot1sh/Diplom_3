import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти элементы")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step("Получить текст элемента")
    def text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Проверить URL")
    def url_contains(self, value):
        return bool(self.wait.until(lambda driver: value in driver.current_url))

    @allure.step("Проверить точный URL")
    def url_is(self, url):
        return bool(self.wait.until(lambda driver: driver.current_url.rstrip("/") == url.rstrip("/")))

    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()

    @allure.step("Прокрутить к элементу")
    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element,
        )

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Проверить наличие элементов")
    def has_elements(self, locator):
        return bool(self.find_all(locator))

    @allure.step("Проверить, что модальное окно исчезло")
    def wait_modal_closed(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step("Получить текст элемента")
    def text(self, locator):
        return self.wait_visible(locator).text

    @allure.step("Проверить URL")
    def url_contains(self, value):
        self.wait.until(lambda d: value in d.current_url)

    @allure.step("Проверить, что модальное окно исчезло")
    def wait_modal_closed(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

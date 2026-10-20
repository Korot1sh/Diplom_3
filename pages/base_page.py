from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def text(self, locator):
        return self.find(locator).text

    def wait_url_contains(self, value):
        self.wait.until(EC.url_contains(value))

    def close_modal(self):
        self.click((By.XPATH, "//div[contains(@class,'modal')]//button"))

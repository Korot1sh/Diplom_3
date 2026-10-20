import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.api_client import StellarApi
from utils.test_data import unique_user


BASE_URL = "https://qa-stellarburgers.education-services.ru"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="all",
        choices=["all", "chrome", "firefox"],
        help="Browser: chrome, firefox or all",
    )


def _driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1440,1000")
        return webdriver.Chrome(options=options)
    options = FirefoxOptions()
    options.add_argument("--width=1440")
    options.add_argument("--height=1000")
    return webdriver.Firefox(options=options)


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        selected = metafunc.config.getoption("--browser")
        browsers = ["chrome", "firefox"] if selected == "all" else [selected]
        metafunc.parametrize("browser_name", browsers)


@pytest.fixture
def driver(browser_name):
    driver = _driver(browser_name)
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def api(base_url):
    return StellarApi(base_url)


@pytest.fixture
def user(api):
    data = unique_user()
    body = api.register(data)
    token = body["accessToken"]
    user_data = {"data": data, "token": token}
    yield user_data
    response = api.delete_user(token)
    if response.status_code not in (200, 202):
        allure.attach(
            response.text,
            name="delete-user-response",
            attachment_type=allure.attachment_type.TEXT,
        )


@pytest.fixture
def auth_context(driver, base_url, user):
    from pages.login_page import LoginPage
    
    login = LoginPage(driver)
    login.open_login(base_url)
    login.login(user["data"]["email"], user["data"]["password"])
    AccountPage(driver).open_account(base_url)
    return user


@pytest.fixture
def order_ingredients(api):
    ingredients = api.ingredients()
    bun = next(x for x in ingredients if x["type"] == "bun")
    filling = next(x for x in ingredients if x["type"] != "bun")
    return [bun["_id"], filling["_id"]], bun["name"], filling["name"]

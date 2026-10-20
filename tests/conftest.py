import os
import uuid

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.login_page import LoginPage

BASE_URL = os.getenv("BASE_URL", "https://qa-stellarburgers.education-services.ru")
API_URL = os.getenv("API_URL", BASE_URL.rstrip("/") + "/api")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1440,1000")
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("--width=1440")
        options.add_argument("--height=1000")
        browser = webdriver.Firefox(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


def make_user():
    email = f"diplom_{uuid.uuid4().hex[:10]}@example.com"
    password = "Qwerty12345!"
    name = "Diplom Test"
    return {"email": email, "password": password, "name": name}


@pytest.fixture
def user():
    data = make_user()
    response = requests.post(f"{API_URL}/auth/register", json=data, timeout=15)
    response.raise_for_status()
    body = response.json()
    token = body["accessToken"]
    yield {**data, "token": token}
    try:
        requests.delete(f"{API_URL}/auth/user", headers={"Authorization": token}, timeout=15)
    except requests.RequestException:
        pass


@pytest.fixture
def logged_in(driver, user):
    LoginPage(driver).login(user["email"], user["password"])
    return user


# Legacy API fixtures are kept so the repository's original API checks can run too.
@pytest.fixture
def created_user():
    data = make_user()
    response = requests.post(f"{API_URL}/auth/register", json=data, timeout=15)
    response.raise_for_status()
    body = response.json()
    token = body["accessToken"]
    yield data, token
    try:
        requests.delete(f"{API_URL}/auth/user", headers={"Authorization": token}, timeout=15)
    except requests.RequestException:
        pass


@pytest.fixture
def ingredients():
    response = requests.get(f"{API_URL}/ingredients", timeout=15)
    response.raise_for_status()
    return [item["_id"] for item in response.json()["data"][:2]]

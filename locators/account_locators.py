from selenium.webdriver.common.by import By

PROFILE_EMAIL = (By.NAME, "name")
PROFILE_NAME = (By.NAME, "name")
HISTORY_LINK = (By.XPATH, "//a[contains(normalize-space(), 'История заказов')]")
LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
ACCOUNT_HEADER = (By.XPATH, "//*[contains(normalize-space(), 'Личный кабинет')]")

from selenium.webdriver.common.by import By

EMAIL = (By.NAME, "name")
RECOVER_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
SHOW_PASSWORD_BUTTON = (
    By.CSS_SELECTOR,
    "div[class*='input__icon'], div[class*='input__icon_action']"
)
PASSWORD_INPUT = (By.NAME, "Пароль")
LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")

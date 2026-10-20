from selenium.webdriver.common.by import By

PASSWORD = (By.NAME, "Пароль")
SHOW_PASSWORD_BUTTON = (
    By.CSS_SELECTOR,
    "div[class*='input__icon'], div[class*='input__icon_action']"
)
RESET_BUTTON = (By.XPATH, "//button[normalize-space()='Сохранить']")

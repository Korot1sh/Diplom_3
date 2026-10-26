from selenium.webdriver.common.by import By

EMAIL = (By.NAME, "name")
PASSWORD = (By.NAME, "Пароль")
LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Восстановить пароль']")
REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")

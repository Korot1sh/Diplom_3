from selenium.webdriver.common.by import By

FEED_HEADER = (By.XPATH, "//*[normalize-space()='Лента заказов']")
ORDER_CARD = (
    By.XPATH,
    "//*[contains(@class,'OrderHistory') or contains(@class,'OrderFeed') or contains(@class,'OrderCard')]"
)
TOTAL_ALL = (By.XPATH, "//*[contains(normalize-space(), 'Выполнено за все время')]/following::*[1]")
TOTAL_TODAY = (By.XPATH, "//*[contains(normalize-space(), 'Выполнено за сегодня')]/following::*[1]")
IN_PROGRESS = (By.XPATH, "//*[contains(normalize-space(), 'В работе')]/following::*[1]")
MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal']")
MODAL_CLOSE = (By.CSS_SELECTOR, "div[class*='Modal_modal'] button[class*='close']")
MODAL_ORDER_NUMBER = (
    By.CSS_SELECTOR,
    "div[class*='Modal_modal'] h2, div[class*='Modal_modal'] [class*='OrderDetails_number']"
)

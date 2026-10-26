from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (By.XPATH, "//a[normalize-space()='Конструктор']")
FEED_LINK = (By.XPATH, "//a[contains(normalize-space(), 'Лента заказов')]")
INGREDIENT_CARD = (
    By.XPATH,
    "//p[normalize-space()='{name}']/ancestor::*[contains(@class,'BurgerIngredient_ingredient')][1]"
)
INGREDIENT_NAME = (By.XPATH, ".//p[normalize-space()='{name}']")
INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter__num'], div[class*='counter__num']")
MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal']")
MODAL_TITLE = (By.CSS_SELECTOR, "div[class*='Modal_modal'] h2")
MODAL_CLOSE = (By.CSS_SELECTOR, "div[class*='Modal_modal'] button[class*='close']")
ORDER_BUTTON = (By.XPATH, "//button[contains(normalize-space(), 'Оформить заказ')]")
CONSTRUCTOR_AREA = (
    By.CSS_SELECTOR,
    "div[class*='BurgerConstructor_basket'], section[class*='BurgerConstructor_basket']"
)
ORDER_MODAL_NUMBER = (
    By.CSS_SELECTOR,
    "div[class*='Modal_modal'] [class*='OrderDetails_number'], div[class*='Modal_modal'] h2"
)

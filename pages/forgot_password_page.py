from selenium.webdriver.common.by import By
from .base_page import BasePage


class ForgotPasswordPage(BasePage):
    EMAIL = (By.XPATH, "//input[@type='text' or @type='email']")
    RESTORE = (By.XPATH, "//button[contains(normalize-space(),'Восстановить')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD = (By.XPATH, "//*[contains(@class,'input') or contains(@class,'password')]//*[name()='svg' or @role='button']")

    def restore(self, email):
        self.find(self.EMAIL).send_keys(email)
        self.click(self.RESTORE)

    def password_is_active(self):
        field = self.find(self.PASSWORD)
        return field.get_attribute('class') or ''

    def toggle_password(self):
        field = self.find(self.PASSWORD)
        # The eye control is usually a sibling of the password input.
        self.driver.execute_script(
            "const i=arguments[0]; const p=i.parentElement; const c=p.querySelector('svg,button,[role=button]'); if(c)c.click();",
            field,
        )

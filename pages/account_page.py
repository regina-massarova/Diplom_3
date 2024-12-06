from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from config import BASE_URL


class AccountPage(BasePage):
    def click_account_button(self):
        wait = WebDriverWait(self.driver, 10)
        self.wait_for_element_visible(AccountPageLocators.ORDER_BUTTON)
        account_button = wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BUTTON))
        account_button.click()


    def click_order_history_button(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    def is_order_completed(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_COMPLETED) == "Выполнен"

    def is_login_button_visible_after_logout(self):
        return self.get_text_from_element(AccountPageLocators.LOGIN_AFTER_LOGOUT) == "Вход"

    def open_login_page(self):
        self.navigate_to(f"{BASE_URL}/login")

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_with_js(AccountPageLocators.LOGIN_BUTTON)
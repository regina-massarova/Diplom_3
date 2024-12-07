from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from config import BASE_URL

class ForgotPasswordPage(BasePage):
    def open_login_page(self):
        self.navigate_to(f"{BASE_URL}/login")

    def navigate_to_forgot_password_page(self):
        self.click_to_element(ForgotPasswordLocators.RECOVER_PASSWORD_BUTTON)

    def enter_email(self, email):
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click_to_element(ForgotPasswordLocators.RECOVER_BUTTON)

    def toggle_password_visibility(self):
        self.click_to_element(ForgotPasswordLocators.TOGGLE_PASSWORD_BUTTON)

    def get_password_input_type(self):
        return self.get_element_attribute(ForgotPasswordLocators.NEW_PASSWORD_INPUT, "type")

    def is_recover_button_visible(self):
        return self.find_element_with_wait(ForgotPasswordLocators.RECOVER_BUTTON)

    def is_new_password_input_visible(self):
        return self.find_element_with_wait(ForgotPasswordLocators.NEW_PASSWORD_INPUT)
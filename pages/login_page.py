from .base_page import BasePage
from .locators import RegistrationFormLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*RegistrationFormLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        one_password_input = self.browser.find_element(*RegistrationFormLocators.ONE_PASSWORD_INPUT)
        one_password_input.send_keys(password)
        second_password_input = self.browser.find_element(*RegistrationFormLocators.SECOND_PASSWORD_INPUT)
        second_password_input.send_keys(password)
        registration_button = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_BUTTON)
        registration_button.click()

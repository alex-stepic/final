from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login")>0, f'String "{self.browser.current_url}" is not login url'
        #assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email, password):

        xemail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        xemail.send_keys(email)

        xpassword1=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        xpassword1.send_keys(password)

        xpassword2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        xpassword2.send_keys(password)

        xbutton=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        xbutton.click()
        
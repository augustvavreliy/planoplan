from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPopupLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def should_be_login_button(self):
        assert self.is_element_present(
            *MainPageLocators.MAIN_LOGIN_BUTTON), "Login button is not presented"

    def go_to_login_popup(self):
        login_button = self.browser.find_element(
            *MainPageLocators.MAIN_LOGIN_BUTTON)
        login_button.click()

    def should_be_login_popup(self):
        assert self.is_element_present(
            *LoginPopupLocators.FORM_POPUP), "Login form is not presented"

    def go_to_singup_popup(self):
        login_button = self.browser.find_element(
            *LoginPopupLocators.SINGUP_POPUP)
        login_button.click()

    def send_email_and_password(self):
        # email = self.browser.find_element(*LoginPopupLocators.EMAIL)
        # email.send_keys("Petrov")
        # password = self.browser.find_element(*LoginPopupLocators.PASSWORD)
        # password.send_keys("KiKi")
        email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPopupLocators.EMAIL))
        email.send_keys("fillion10@mail.com")
        password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPopupLocators.PASSWORD))
        password.send_keys("123was123")

    def press_singup_button(self):
        singup_button = self.browser.find_element(
            *LoginPopupLocators.SINGUP_BUTTON)
        singup_button.click()

    def should_be_code_popup(self):
        # assert self.is_element_present(
        #    *LoginPopupLocators.CODE_INPUT), "Code form is not presented"
        
        input_code = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(LoginPopupLocators.CODE_INPUT))
from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_LOGIN_BUTTON = (By.CLASS_NAME, "widget-button__CabinetLinkButton-sc-7ezmr3-3")

class LoginPopupLocators():
    FORM_POPUP = (By.ID, "form-entry")
    SINGUP_POPUP = (By.CSS_SELECTOR, "button[data-test='button_signup']")
    EMAIL = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[autocomplete='new-password']")
    SINGUP_BUTTON = (By.CSS_SELECTOR, "button[data-test='signup_submit']")
    CODE_INPUT = (By.CSS_SELECTOR, "input[name='code']")
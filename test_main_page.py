from .pages.main_page import MainPage


def test_user_can_go_to_login_page(browser):
    link = "https://planoplan.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_popup()

def test_user_can_go_to_singup_popup(browser):
    link = "https://planoplan.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_popup()
    page.go_to_singup_popup()

def test_user_can_write_in_form(browser):
    link = "https://planoplan.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_popup()
    page.go_to_singup_popup()
    page.send_email_and_password()

def test_user_can_register(browser):
    link = "https://planoplan.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_popup()
    page.go_to_singup_popup()
    page.send_email_and_password()
    page.press_singup_button()
    page.should_be_code_popup()
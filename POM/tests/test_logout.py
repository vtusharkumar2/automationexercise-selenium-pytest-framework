from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_logout(driver):
    login = LoginPage(driver)
    home = HomePage(driver)
    login.load()
    login.enter_email("vtusharkumar1010312@gmail.com")
    login.enter_password("qwerty123")
    login.click_login()

    home.click_logout()

    assert "login" in driver.current_url




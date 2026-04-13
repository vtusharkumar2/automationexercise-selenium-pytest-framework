from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_login(driver):
    login = LoginPage(driver)
    login.enter_email("vtusharkumar1010312@gmail.com")
    login.enter_password("qwerty123")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in login.get_logged_in_text()


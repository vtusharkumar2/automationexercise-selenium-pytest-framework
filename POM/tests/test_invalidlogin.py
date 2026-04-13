from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.enter_email("invalidemail@gmail.com")
    login.enter_password("invalidpass") 
    login.click_login()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Your email or password is incorrect!')]")
    ))

    assert "Your email or password is incorrect" in login.get_error_message()
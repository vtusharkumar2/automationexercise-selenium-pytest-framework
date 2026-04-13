from pages.sign_up_page import SignUpPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_existing_email(driver):
    signup = SignUpPage(driver)
    signup.load()
    signup.enter_name("tusharvinod")
    signup.enter_email("vtusharkumar1010312@gmail.com")
    signup.click_login()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Email Address already exist!')]"))
    )

    assert "Email Address already exist!" in signup.get_error_message()
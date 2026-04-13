from pages.login_page import LoginPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_empty_cart_checkout(driver):
    login = LoginPage(driver)
    cart = CartPage(driver)


    login.load()

    login.enter_email("vtusharkumar1010312@gmail.com")

    login.enter_password("qwerty123")

    login.click_login()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in login.get_logged_in_text()

    cart.load()
    

    assert not cart.is_checkout_button_present(), "Checkout button should not be visible for empty cart"
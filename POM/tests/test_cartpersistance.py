from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import Productspage
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_cart_persistance(driver):
    login = LoginPage(driver)
    cart = CartPage(driver)
    product = Productspage(driver)
    home = HomePage(driver)

   

    product.load()

    product.addproduct1()

    product.continuebutton()

    login.load()

    login.enter_email("vtusharkumar1010312@gmail.com")

    login.enter_password("qwerty123")

    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in login.get_logged_in_text()

    cart.load()

    assert "Blue Top" in cart.product1name()



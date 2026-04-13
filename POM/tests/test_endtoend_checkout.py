from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import Productspage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlaced


def test_end_to_end_checkout(driver):
    login = LoginPage(driver)
    cart = CartPage(driver)
    product = Productspage(driver)
    checkout = CheckoutPage(driver)
    payment = PaymentPage(driver)
    order = OrderPlaced(driver)


    login.load()

    login.enter_email("vtusharkumar1010312@gmail.com")

    login.enter_password("qwerty123")

    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in login.get_logged_in_text()

    product.load()

    product.addproduct1()

    product.continuebutton()

    product.addproduct2()

    product.continuebutton()

    cart.load()

    cart.click_checkoutbutton()

    checkout.enter_message("very good harasment!")

    checkout.click_place_order()

    payment.enter_name("Tushar V")

    payment.enter_card_number("123456")

    payment.enter_cvc("321")

    payment.enter_expiry_month("12")

    payment.enter_expiration_year("1919")

    payment.click_confirm_order()

    assert "ORDER PLACED!" in order.get_order_confirm_text()

    order.click_continue_button()

    

    assert driver.current_url == "https://automationexercise.com/"


    
















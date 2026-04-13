from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import Productspage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    login = LoginPage(driver)
    cart = CartPage(driver)
    product = Productspage(driver)
    checkout = CheckoutPage(driver)

    login.load()

    login.enter_email("vtusharkumar1010312@gmail.com")

    login.enter_password("qwerty123")

    login.click_login()

    product.load()

    product.addproduct1()

    product.continuebutton()

    product.addproduct2()

    cart.load()

    cart.click_checkoutbutton()

    assert checkout.is_checkout_loaded()

    assert "kumar" in checkout.get_name()

    assert "12/7 htype khamaria" in checkout.get_address_loc()

    assert "jabalpur mp 482005" in checkout.get_city_loc()






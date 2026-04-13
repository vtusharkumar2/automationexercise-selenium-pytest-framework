from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.products_page import Productspage
from pages.cart_page import CartPage


def test_cart(driver):
    product = Productspage(driver)
    cart = CartPage(driver)

    product.load()

    # Add first product
    product.addproduct1()
    product.continuebutton()

    # Add second product
    product.addproduct2()
    product.continuebutton()

    # Go to cart
    cart.load()

    # Assertions
    assert "Blue Top" in cart.product1name()
    assert "Men Tshirt" in cart.product2name()
   
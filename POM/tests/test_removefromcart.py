from pages.cart_page import CartPage
from pages.products_page import Productspage

def test_remove_fromcart(driver):
    cart  = CartPage(driver)
    product = Productspage(driver)

    product.load()

    product.addproduct1()

    product.continuebutton()


    cart.load()

    cart.remove_product1()

    

    assert cart.is_cart_empty()
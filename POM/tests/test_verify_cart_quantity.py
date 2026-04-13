from pages.product_detail_page import ProductDetail
from pages.cart_page import CartPage


def test_verify_cart_quantity(driver):
    productd= ProductDetail(driver)
    cart = CartPage(driver)

    productd.load()

    productd.update_product_quantity(90)

    productd.click_add_to_cart_button()

    productd.click_continue_button()

    cart.load()

    assert cart.get_cart_quantity() == "90"

    


    


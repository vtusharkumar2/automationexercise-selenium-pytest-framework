from pages.products_page import Productspage


def test_search_dress(driver):
    product = Productspage(driver)

    product.load()

    product.search_product("Blue Top")

    results = product.get_search_results()

    for name in results:
        assert "Blue Top" in name

    





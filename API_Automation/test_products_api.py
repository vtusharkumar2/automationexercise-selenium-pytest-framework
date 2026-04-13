from base.api_client import APIClient

def test_get_all_products():

    client = APIClient()

    response = client.get("/productsList")

    assert response.status_code == 200, "Status code is not 200"

    data = response.json()

    assert "products" in data, "Products key missing in response"

    assert len(data["products"]) > 0, "No products found"
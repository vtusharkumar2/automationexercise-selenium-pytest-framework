from base.api_client import APIClient

def test_invalid_searching():
    client = APIClient()
    payload = {"search_product": "xyz121"}

    response = client.post("/searchProduct",payload = payload)

    assert response.status_code == 200

    result = response.json()

    assert "products" in result
    assert len(result["products"]) == 0


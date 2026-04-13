from base.api_client import APIClient

def test_post_products_not_allowed():
    client = APIClient()

    payload = {
        "title": "Test Product",
        "price": 500
    }

    response = client.post("/products", payload=payload)

    assert response.status_code == 404

from base.api_client import APIClient

def test_search_product():
    client = APIClient()

    payload = {"search_product" : "top"} 

    response = client.post("/searchProduct",payload = payload)
    assert response.status_code  == 200

    result = response.json()
    assert "products" in result

    assert len(result["products"])>0
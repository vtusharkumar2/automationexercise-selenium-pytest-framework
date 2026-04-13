from base.api_client import APIClient


def test_put_brand_negative():
    client = APIClient()

    response = client.put("/brandsList",payload = {})

    assert response.status_code == 200

    assert "this request method is not supported" in response.json()["message"].lower()
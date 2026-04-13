from base.api_client import APIClient


def test_get_brands_list():
    client = APIClient()

    response= client.get("/brandsList")

    assert response.status_code == 200

    data = response.json()

    assert "brands" in data
    assert len(data["brands"]) > 0


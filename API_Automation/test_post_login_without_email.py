from base.api_client import APIClient

def test_post_login_withno_email():
    client = APIClient()
    payload = {"password": "qwerty123"}

    response = client.post("/verifyLogin",payload = payload)

    assert response.status_code == 200

    result = response.json()

    assert "message" in result

    assert "email or password parameter is missing" in result["message"].lower()


from base.api_client import APIClient

def test_valid_login():
    client = APIClient()

    payload = {"email":"vtusharkumar1010312@gmail.com",
               "password": "qwerty123"}

    response = client.post("/verifyLogin",payload = payload)

    assert response.status_code == 200

    result = response.json()

    assert "message" in result,  "message key missing"

    assert result["message"] == "User exists!"
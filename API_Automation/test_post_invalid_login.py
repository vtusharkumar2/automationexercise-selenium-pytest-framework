from base.api_client import APIClient

def test_post_invalid_login():
    client = APIClient()

    payload = {"email": "vtusharkumar2@gmail.com",
                 "password": "incorrect"}

    response = client.post("/verifyLogin",payload = payload)

    assert response.status_code == 200



    result = response.json()

    assert "message" in result , "user not found"

    assert result["message"] == "User not found!"
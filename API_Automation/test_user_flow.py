from base.api_client import APIClient
import random

def test_user_flow():
    client = APIClient()
    email = f"vtusharkumar{random.randint(10,10000)}@gmail.com"
    password = "qwerty123"

    register_payload = {
        "name": "Tushar",
        "email": email,
        "password": password,
        "title": "Mr.",
        "birth_date": "19",
        "birth_month": "10",
        "birth_year": "2004",
        "firstname": "Tushar",
        "lastname": "Kumar",
        "company": "webyalaya",
        "address1": "abc",
        "country": "India",
        "zipcode": "482005",
        "state": "MP",
        "city": "Jabalpur",
        "mobile_number": "9999999999"
        }

    response = client.post("/createAccount", payload=register_payload)
    assert response.status_code == 200
    assert "user created!" in response.json()["message"].lower()

    login_payload = {"email":email,"password":password}
    response = client.post("/verifyLogin", payload=login_payload)
    assert "user exists!" in response.json()["message"].lower()

    assert response.status_code == 200

    response = client.get(f"/getUserDetailByEmail?email={email}")
    assert response.status_code == 200
    data = response.json()

    assert "user" in data
    assert data["user"]["email"] == email

    response = client.delete("/deleteAccount",payload={"email": email, "password": password})
    assert response.status_code == 200

    assert "account deleted" in response.json()["message"].lower()




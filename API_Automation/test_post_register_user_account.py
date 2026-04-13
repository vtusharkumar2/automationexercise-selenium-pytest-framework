from base.api_client import APIClient
import random


def test_post_register_user():

    client = APIClient()
    email = f"vtusharkumar{random.randint(10,10000)}@gmail.com"

    payload = {"name": "Tushar",
                "email":email,
                "password":"qwerty123",
                "title":"Mr.",
                "birth_date":"19",
                "birth_month":"10",
                "birth_year":"2004",
                "firstname":"Tushar",
                "lastname":"Kumar",
                "company":"webyalaya",
                "address1":"12/7 htype khamaria jbp",
                "address2":"none",
                "country":"India",
                "zipcode":"482005",
                "state":"Mp",
                "city":"jabalpur",
                "mobile_number":"1137131422"}

    response = client.post("/createAccount",payload = payload)

    assert response.status_code == 200

    result = response.json()

    assert "message" in result

    assert "user created" in result["message"].lower(), "User creation failed"


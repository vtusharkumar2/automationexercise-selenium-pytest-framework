import requests
BASE_URL = "https://automationexercise.com/api"

class APIClient:

    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None):
        return requests.get(
            self.base_url + endpoint,
            params=params
        )

    def post(self, endpoint, payload=None):
        return requests.post(
            self.base_url + endpoint,
            data=payload
        )

    def put(self, endpoint, payload=None):
        return requests.put(
            self.base_url + endpoint,
            json=payload
        )

    def delete(self, endpoint, payload=None):
        return requests.delete(
        self.base_url + endpoint,
        data=payload   
        )
import requests


class StellarApi:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def register(self, user):
        response = self.session.post(
            f"{self.base_url}/api/auth/register",
            json=user,
            timeout=20,
        )
        response.raise_for_status()
        body = response.json()
        assert body["success"], body
        return body

    def login(self, email, password):
        response = self.session.post(
            f"{self.base_url}/api/auth/login",
            json={"email": email, "password": password},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, token):
        response = self.session.delete(
            f"{self.base_url}/api/auth/user",
            headers={"Authorization": token},
            timeout=20,
        )
        return response

    def ingredients(self):
        response = self.session.get(
            f"{self.base_url}/api/ingredients", timeout=20
        )
        response.raise_for_status()
        return response.json()["data"]

    def create_order(self, token, ingredient_ids):
        response = self.session.post(
            f"{self.base_url}/api/orders",
            json={"ingredients": ingredient_ids},
            headers={"Authorization": token},
            timeout=20,
        )
        response.raise_for_status()
        body = response.json()
        assert body["success"], body
        return body

    def user_orders(self, token):
        response = self.session.get(
            f"{self.base_url}/api/orders",
            headers={"Authorization": token},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()["orders"]

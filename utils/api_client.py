import allure
import requests

from .constants import (
    API_INGREDIENTS,
    API_LOGIN,
    API_ORDERS,
    API_REGISTER,
    API_USER,
)


class StellarApi:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    @allure.step("API: зарегистрировать пользователя")
    def register(self, user):
        response = self.session.post(
            f"{self.base_url}{API_REGISTER}",
            json=user,
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    @allure.step("API: авторизовать пользователя")
    def login(self, email, password):
        response = self.session.post(
            f"{self.base_url}{API_LOGIN}",
            json={"email": email, "password": password},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    @allure.step("API: удалить пользователя")
    def delete_user(self, token):
        return self.session.delete(
            f"{self.base_url}{API_USER}",
            headers={"Authorization": token},
            timeout=20,
        )

    @allure.step("API: получить список ингредиентов")
    def ingredients(self):
        response = self.session.get(
            f"{self.base_url}{API_INGREDIENTS}",
            timeout=20,
        )
        response.raise_for_status()
        return response.json()["data"]

    @allure.step("API: создать заказ")
    def create_order(self, token, ingredient_ids):
        response = self.session.post(
            f"{self.base_url}{API_ORDERS}",
            json={"ingredients": ingredient_ids},
            headers={"Authorization": token},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    @allure.step("API: получить заказы пользователя")
    def user_orders(self, token):
        response = self.session.get(
            f"{self.base_url}{API_ORDERS}",
            headers={"Authorization": token},
            timeout=20,
        )
        response.raise_for_status()
        return response.json()["orders"]

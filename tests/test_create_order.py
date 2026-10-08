import allure
import requests

from tests.conftest import BASE_URL


ORDERS_ENDPOINT = "/api/orders"


@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_authorization(self, created_user, ingredients):
        _, access_token = created_user

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            headers={"Authorization": access_token},
            json={"ingredients": ingredients},
            timeout=20,
        )

        assert response.status_code == 200
        body = response.json()
        assert body["success"] is True
        assert body["order"]["number"]

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_without_authorization(self, ingredients):
        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": ingredients},
            timeout=20,
        )

        assert response.status_code == 200
        body = response.json()
        assert body["success"] is True
        assert body["order"]["number"]

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_with_authorization_without_ingredients(self, created_user):
        _, access_token = created_user

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            headers={"Authorization": access_token},
            json={},
            timeout=20,
        )

        assert response.status_code == 400
        assert response.json() == {
            "success": False,
            "message": "Ingredient ids must be provided",
        }

    @allure.title("Создание заказа без авторизации и без ингредиентов")
    def test_create_order_without_authorization_without_ingredients(self):
        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={},
            timeout=20,
        )

        assert response.status_code == 400
        assert response.json() == {
            "success": False,
            "message": "Ingredient ids must be provided",
        }

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self, created_user):
        _, access_token = created_user

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            headers={"Authorization": access_token},
            json={"ingredients": ["invalid_ingredient_hash"]},
            timeout=20,
        )

        assert response.status_code == 500
        assert "Internal Server Error" in response.text

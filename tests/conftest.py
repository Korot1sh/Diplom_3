import uuid

import allure
import pytest
import requests

from tests.constants import (
    BASE_URL,
    INGREDIENTS_ENDPOINT,
    LOGIN_ENDPOINT,
    REGISTER_ENDPOINT,
    USER_ENDPOINT,
)


def unique_user():
    suffix = uuid.uuid4().hex
    return {
        "email": f"api_test_{suffix}@example.com",
        "password": f"TestPassword_{suffix}",
        "name": f"Api Test {suffix}",
    }


def register_user(user):
    response = requests.post(
        f"{BASE_URL}{REGISTER_ENDPOINT}",
        json=user,
        timeout=20,
    )
    return response


def login_user(user):
    response = requests.post(
        f"{BASE_URL}{LOGIN_ENDPOINT}",
        json={"email": user["email"], "password": user["password"]},
        timeout=20,
    )
    return response


def delete_user(access_token):
    return requests.delete(
        f"{BASE_URL}{USER_ENDPOINT}",
        headers={"Authorization": access_token},
        timeout=20,
    )


@pytest.fixture
def created_user():
    user = unique_user()
    response = register_user(user)
    assert response.status_code == 200, response.text

    body = response.json()
    assert body["success"] is True
    access_token = body["accessToken"]

    yield user, access_token

    with allure.step("Удалить тестового пользователя"):
        delete_response = delete_user(access_token)
        assert delete_response.status_code in (200, 202), delete_response.text


@pytest.fixture
def ingredients():
    response = requests.get(
        f"{BASE_URL}{INGREDIENTS_ENDPOINT}",
        timeout=20,
    )
    assert response.status_code == 200, response.text

    body = response.json()
    assert body["success"] is True
    assert body["data"]

    return [item["_id"] for item in body["data"][:2]]

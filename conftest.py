import requests
import pytest
import faker
import allure

from data.urls import MAIN_URL, CREATE_USER, LOGIN_USER, DELETE_USER

@allure.title('Создание пользователя')
@pytest.fixture
def create_user(generate_user):
    response = requests.post(MAIN_URL + CREATE_USER, data=generate_user)
    yield response
    requests.delete(MAIN_URL + DELETE_USER, headers={'Authorization': response.json()['accessToken']})

@allure.title('Генерация данных пользователя')
@pytest.fixture
def generate_user():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@allure.title('Авторизация пользователя')
@pytest.fixture
def login_user(generate_user):
    requests.post(MAIN_URL + CREATE_USER, data=generate_user)
    response = requests.post(MAIN_URL + LOGIN_USER, data=generate_user)
    yield response
    requests.delete(MAIN_URL + DELETE_USER, headers={'Authorization': response.json()['accessToken']})




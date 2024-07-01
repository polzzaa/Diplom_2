from data.urls import MAIN_URL, CREATE_USER, LOGIN_USER, CHANGE_DATA, CREATE_ORDER

import requests
import faker
import allure

@allure.title('Генерация имени')
def generate_name():
    fake = faker.Faker()
    return fake.name()

@allure.title('Генерация почты')
def generate_email():
    fake = faker.Faker()
    return fake.email()

@allure.title('Генерация пароля')
def generate_password():
    fake = faker.Faker()
    return fake.random_int(10)

@allure.title('Создание пользователя')
def create_user(payload):
    return requests.post(MAIN_URL + CREATE_USER, data=payload)

@allure.title('Авторизация пользователя')
def login_user(payload):
    return requests.post(MAIN_URL + LOGIN_USER, data=payload)

@allure.title('Изменение данных пользователя')
def change_data(payload):
    r = requests.post(MAIN_URL + CREATE_USER, data=payload)
    return requests.patch(MAIN_URL + CHANGE_DATA, data=payload,
                          headers={'Authorization': r.json()['accessToken']})

@allure.title('Изменение данных пользователя без авторизации')
def change_data_without_autorization(payload):
    return requests.patch(MAIN_URL + CHANGE_DATA, data=payload)

def create_order(payload, login):
    return requests.post(MAIN_URL + CREATE_ORDER, data=payload,
                             headers={'Authorization': login.json()['accessToken']})

def create_order_without_authorazation(payload):
    return requests.post(MAIN_URL + CREATE_ORDER, data=payload)


from urls import MAIN_URL, CREATE_ORDER
import requests
import allure


class TestCreateOrder:

    @allure.title('Тест на создание заказа с авторизацией')
    def test_create_order(self, login_user):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        response = requests.post(MAIN_URL + CREATE_ORDER, data=payload,
                                 headers={'Authorization': login_user.json()['accessToken']})

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест на создание заказа без авторизации')
    def test_create_order_without_authorization(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
        response = requests.post(MAIN_URL + CREATE_ORDER, data=payload)

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест на создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, login_user):
        response = requests.post(MAIN_URL + CREATE_ORDER,
                                 headers={'Authorization': login_user.json()['accessToken']})

        assert response.status_code == 400 and response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title('Тест на создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, login_user):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa", "61c0c5a71d1f82001bdaaa"]}
        response = requests.post(MAIN_URL + CREATE_ORDER, data=payload,
                                 headers={'Authorization': login_user.json()['accessToken']})

        assert response.status_code == 500
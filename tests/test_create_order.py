from helpers import create_order, create_order_without_authorazation
from data.ingredient import Ingredients
from data.status_code import StatusCode

import allure


class TestCreateOrder:

    @allure.title('Тест на создание заказа с авторизацией')
    def test_create_order(self, login_user):
        response = create_order(Ingredients.ingredients, login_user)

        assert response.status_code == StatusCode.OK and response.json()['success']


    @allure.title('Тест на создание заказа без авторизации')

    def test_create_order_without_authorization(self):
        response = create_order_without_authorazation(Ingredients.ingredients)

        assert response.status_code == StatusCode.OK and response.json()['success']

    @allure.title('Тест на создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, login_user):
        response = create_order(Ingredients.without_ingredients, login_user)

        assert response.status_code == StatusCode.BAD_REQUEST and response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title('Тест на создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, login_user):
        response = create_order(Ingredients.incorrect_ingredients, login_user)

        assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR
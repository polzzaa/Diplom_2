from data.urls import MAIN_URL, GET_ORDERS
from helpers import create_order
from data.ingredient import Ingredients
from data.status_code import StatusCode
import requests
import allure

class TestGetOrders:

    @allure.title('Тест получение заказов конкретного пользователя')
    def test_get_orders(self, login_user):
        create_order(Ingredients.ingredients, login_user)
        response = requests.get(MAIN_URL + GET_ORDERS, headers={'Authorization': login_user.json()['accessToken']})
        assert response.status_code == StatusCode.OK and response.json()['success'] == True

    @allure.title('Тест на получение заказов конкретного пользователя без авторизации')
    def test_orders_without_authorization(self):
        response = requests.get(MAIN_URL + GET_ORDERS)
        assert response.status_code == StatusCode.UNAUTHORIZED and response.text == '{"success":false,"message":"You should be authorised"}'



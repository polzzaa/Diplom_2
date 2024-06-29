from urls import MAIN_URL, GET_ORDERS
import requests
import allure

class TestGetOrders:

    @allure.title('Тест получение заказов конкретного пользователя')
    def test_get_orders(self, login_user):
        response = requests.get(MAIN_URL + GET_ORDERS, headers={'Authorization': login_user.json()['accessToken']})
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Тест на получение заказов конкретного пользователя без авторизации')
    def test_orders_without_authorization(self):
        response = requests.get(MAIN_URL + GET_ORDERS)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'



from helpers import change_data, change_data_without_autorization
from data.status_code import StatusCode
import allure

class TestChangeData:

    @allure.title('Тест на изменение данных пользователя с авторизацией')
    def test_change_data(self, generate_user):
        response = change_data(generate_user)
        assert response.status_code == StatusCode.OK and response.json()['success'] == True

    @allure.title('Тест на изменение данных пользователя без авторизации')
    def test_change_data_without_authorization(self, generate_user):
        response = change_data_without_autorization(generate_user)
        assert response.status_code == StatusCode.UNAUTHORIZED and response.text == '{"success":false,"message":"You should be authorised"}'


from helpers import change_data, change_data_without_autorization
import allure

class TestChangeData:

    @allure.title('Тест на изменение данных пользователя с авторизацией')
    def test_change_data(self, generate_user):
        response = change_data(generate_user)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Тест на изменение данных пользователя без авторизации')
    def test_change_data_without_authorization(self, generate_user):
        response = change_data_without_autorization(generate_user)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'


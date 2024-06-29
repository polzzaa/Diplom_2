import pytest
import allure

from helpers import login_user, generate_email, generate_password

class TestLoginUser:

    @allure.title('Тест на авторизацию под существующим пользователем')
    def test_login_user(self, login_user):
        assert login_user.status_code == 200 and login_user.json()['success'] == True

    @allure.title('Тест на авторизацию с неверным логином или паролем')
    @pytest.mark.parametrize('email, password', [['12345', generate_password()], [generate_email(), '12345']])
    def test_login_with_invalid_data(self, email, password, create_user):
        payload = {"email": email, "password": password}
        response = login_user(payload)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"email or password are incorrect"}'


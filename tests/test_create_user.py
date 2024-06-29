from helpers import generate_email, generate_password, generate_name, create_user

import pytest
import allure

class TestCreateUser:

    @allure.title('Тест на создание пользователя')
    def test_create_user(self, create_user):
        assert create_user.status_code == 200 and create_user.json()['success'] == True

    @allure.title('Тест на создание пользователя, который уже зарегистрирован')
    def test_create_two_identical_users(self, generate_user):
        create_user(generate_user)
        response = create_user(generate_user)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Тест на создание пользователя без заполнения одного из обязательных полей')
    @pytest.mark.parametrize('email, password, name', [['', generate_password(), generate_name()],
                                                       [generate_email(), '', generate_name()],
                                                       [generate_email(), generate_password(), '']])
    def test_create_user_without_data(self, email, password, name):
        payload = {"email": email, "password": password, "name": name}
        response = create_user(payload)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"Email, password and name are required fields"}'





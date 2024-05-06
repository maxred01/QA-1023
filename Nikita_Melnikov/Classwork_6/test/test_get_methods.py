import allure
from Maksim_Tsybulka.class_work_5.pages.users_page import UsersPage

users_page = UsersPage()  # Инициализация объекта страницы пользователей


@allure.feature('GET методы')
class TestGetMethods:
    """Тестовый класс для проверки GET запросов"""

    @allure.story('Получение списка пользователей')
    def test_get_users(self):
        """Тест на получение списка всех пользователей"""
        response = users_page.get_users()
        assert response.status_code == 200  # Проверка статуса ответа
        assert 'data' in response.json()  # Проверка наличия данных о пользователях

    @allure.story('Получение пользователя по ID')
    def test_get_user(self):
        """Тест на получение пользователя по ID"""
        response = users_page.get_user(2)
        assert response.status_code == 200  # Проверка статуса ответа
        assert response.json()['data']['id'] == 2  # Проверка ID пользователя

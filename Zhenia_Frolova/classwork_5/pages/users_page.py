import requests
from Maksim_Tsybulka.class_work_5.config import BASE_URL


class UsersPage:
    """Класс Page Object для работы с пользователями на сайте reqres.in"""

    def __init__(self):
        """Инициализация с базовым URL для пользовательских методов"""
        self.sessions = requests.Session()
        self.sessions.headers.update({'Accept': 'application/json'})  # Если api имеет специфический заголовок
        self.users_url = f"{BASE_URL}/users"

    def _requests(self, method, url, **kwargs):
        try:
            response = self.sessions.request(method, url, **kwargs)
            response.raise_for_status()  # Поднимает HTTP ошибку если статус ответа 400 или 500
            return response
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def get_users(self):
        """Получение списка всех пользователей"""
        return self._requests('GET', self.users_url, timeout=5)

    def get_user(self, user_id):
        """Получение пользователя по уникальному идентификатору (ID)"""
        return self._requests('GET', f"{self.users_url}/{user_id}", timeout=5)

    def create_user(self, data):
        """Создание нового пользователя с предоставленными данными"""
        return self._requests('POST', self.users_url, data=data, timeout=5)

    def update_user(self, user_id, data):
        """Обновление данных пользователя по ID"""
        return self._requests('PUT', f"{self.users_url}/{user_id}", data=data, timeout=5)

    def delete_user(self, user_id):
        """Удаление пользователя по ID"""
        return self._requests('DELETE', f"{self.users_url}/{user_id}", timeout=5)

import requests
from Kristina_Pershina.classwork_5.config import BASE_URL


class UsersPage:
    """Класс Page Object для работы с пользователями на сайте reqres.in"""

    def __init__(self):
        """Инициализация с базовым URL для пользовательских методов"""
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json'}) #<If the API has specific header
        self.users_url = f"{BASE_URL}/users"

    def _request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status() #Raises HTTP error in case of 400 or 500 response
            return response
        except requests.exceptions.RequestException as e
            print(e)
            return None

    def get_users(self):
        """Получение списка всех пользователей"""
        return self._request('GET', self.users_url, timeout=5)

    def get_user(self, user_id):
        """Получение пользователя по уникальному идентификатору (ID)"""
        return self._request('GET',f"{self.users_url}/{user_id}", timeout=5)

    def create_user(self, data):
        """Создание нового пользователя с предоставленными данными"""
        return self._request('POST', self.users_url, data=data, timeout=5)

    def update_user(self, user_id, data):
        """Обновление данных пользователя по ID"""
        return self._request('PUT', f"{self.users_url}/{user_id}", data=data, timeout=5)

    def delete_user(self, user_id):
        """Удаление пользователя по ID"""
        return self._request('DELETE', f"{self.users_url}/{user_id}", timeout=5)

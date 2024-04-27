import requests
from Nikita_Balyevich.classwork_6.config import BASE_URL


class UsersPage:
    """Класс Page Object для работы с пользователями на сайте reqres.in"""

    def __init__(self):
        """Инициализация с базовым URL для пользовательских методов"""
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json'})  # If api have specific title
        self.users_url = f"{BASE_URL}/users"
        self.delayed_users_url = f"{BASE_URL}/users?delay=3"

    def __requests(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()  # Up HTTP error if status code 400 or 500
            return response
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def get_users(self):
        """Получение списка всех пользователей"""
        return self.__requests('GET', self.users_url, timeout=5)

    def get_user(self, user_id):
        """Получение пользователя по уникальному идентификатору (ID)"""
        return self.__requests('GET', f"{self.users_url}/{user_id}", timeout=5)

    def create_user(self, data):
        """Создание нового пользователя с предоставленными данными"""
        return self.__requests('POST', self.users_url, data=data, timeout=5)

    def update_user(self, user_id, data):
        """Обновление данных пользователя по ID"""
        return self.__requests('PUT', f"{self.users_url}/{user_id}", data=data, timeout=5)

    def delete_user(self, user_id):
        """Удаление пользователя по ID"""
        return self.__requests('DELETE', f"{self.users_url}/{user_id}", timeout=5)

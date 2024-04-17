import requests
from Maksim_Tsybulka.class_work_5.config import BASE_URL


class UsersPage:
    """Класс Page Object для работы с пользователями на сайте reqres.in"""

    def __init__(self):
        """Инициализация с базовым URL для пользовательских методов"""
        self.users_url = f"{BASE_URL}/users"

    def get_users(self):
        """Получение списка всех пользователей"""
        return requests.get(self.users_url, timeout=5)

    def get_user(self, user_id):
        """Получение пользователя по уникальному идентификатору (ID)"""
        return requests.get(f"{self.users_url}/{user_id}", timeout=5)

    def create_user(self, data):
        """Создание нового пользователя с предоставленными данными"""
        return requests.post(self.users_url, data=data, timeout=5)

    def update_user(self, user_id, data):
        """Обновление данных пользователя по ID"""
        return requests.put(f"{self.users_url}/{user_id}", data=data, timeout=5)

    def delete_user(self, user_id):
        """Удаление пользователя по ID"""
        return requests.delete(f"{self.users_url}/{user_id}", timeout=5)

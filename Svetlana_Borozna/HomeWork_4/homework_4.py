import requests
import pytest_check as check


def test_api_user_not_found():
    r = requests.get('https://reqres.in/api/users/23')
    status_code = r.status_code

    check.equal(status_code, 404, f'Статус код не равен 404. Статус код равен {status_code}')

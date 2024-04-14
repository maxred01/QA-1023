import requests
import pytest_check as check


def test_api_register():

    r = requests.post('https://reqres.in/api/register', json={"email": "eve.holt@reqres.in", "password": "pistol"})
    status_code = r.status_code

    check.equal(status_code, 200, f'Статус код не равен 200. Статус код равен {status_code}')

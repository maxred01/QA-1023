import pytest_check as check
import requests


def test_api_single_user_not_found():
    r = requests.get('https://reqres.in/api/users/23')
    status_code = r.status_code

    check.equal(status_code, 404, f'Status code {status_code}')


def test_api_register_successful():
    r = requests.post("https://reqres.in/api/register",
                      json={"email": "eve.holt@reqres.in", "password": "pistol"})

    check.equal(r.status_code, 200, f'Status code {r.status_code}')

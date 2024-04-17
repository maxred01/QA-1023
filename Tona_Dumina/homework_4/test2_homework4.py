import requests
import pytest_check as check


def test_api_register():
    r = requests.post("https://reqres.in/api/register",
                      json={"email": "eve.holt@reqres.in", "password": "pistol"})

    check.equal(r.status_code, 200, f'Статус код  {r.status_code}')

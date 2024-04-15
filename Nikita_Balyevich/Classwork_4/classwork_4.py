import allure
import pytest_check as check
import requests


# def test_api_users_page():
#     r = requests.get('https://reqres.in/api/users')
#     status_code = r.status_code
#
#     check.equal(status_code, 200, f'Status code is not 200. The code is {status_code}')


@allure.feature('Check /api/users')
def test_api_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    r = requests.post('https://reqres.in/api/users', data=data)
    status_code = r.status_code

    with allure.step("Check status"):
        check.equal(status_code, 201, f'Status != 201. Status = {status_code}')

        print(r.json())

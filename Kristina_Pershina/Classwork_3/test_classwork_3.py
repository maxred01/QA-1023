'''Classwork 3'''

import requests
# import pytest
import pytest_check as check
import allure

# @allure.feature('ID check')
# def test_api_users_page():
#     r = requests.get('https://reqres.in/api/users/2')
#     status_code = r.status_code
#
#     with allure.step('step 1'):
#         check.equal(status_code, 200, f'Status code is not 200. The code is {status_code}')
#
#     with allure.step('step 2'):
#         data = r.json()
#         check.equal(data['data']['id'], 2, f"ID is NOT 2. ID is {data['data']['id']}")


@allure.feature('New user')
def test_api_users_page():
    '''Some func for training'''
    data = {"name": "Vasya",
            "job": "Senior cleaner"
            }
    r = requests.post('https://reqres.in/api/users', data=data, timeout=10)
    status_code = r.status_code

    with allure.step('step 1'):
        check.equal(status_code, 201, f'Status code is not 201. The code is {status_code}')

    with allure.step('step 2'):
        new_user_data = r.json()
        check.equal(new_user_data['name'], 'Vasya', 'Name is wrong.')
        check.equal(new_user_data['job'], 'Senior cleaner', 'Job is wrong.')
    # print(r.json())

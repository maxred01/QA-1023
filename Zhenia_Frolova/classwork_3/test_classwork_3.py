import requests, pytest, pytest_check as check, allure


#@allure.feature ('Проверка /api/users/2')
#def test_api_users_page():
#    r = requests.get('https://reqres.in/api/users/2')
#    status_code = r.status_code
#
#    check.equal(status_code, 200, f'Статус код не равен 200. Статус код равен {status_code}')


#    data = r.json()
#
#    for user in data['data']:
#        check.equal('id' in user and user['id'], '2')

@allure.feature('Проверка /api/user')
def test__api_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    r = requests.post('https://reqres.in/api/users', data=data)
    status_code = r.status_code

    with allure.step('Проверка статус кода'):
        check.equal(status_code, 201, f'Статус код не равен 200. Статус код равен {status_code}')

        print(r.json()
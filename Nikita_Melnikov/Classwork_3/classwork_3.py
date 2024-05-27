import requests, pytest, pytest_check as check, allure


#def test_api_user():
#    r = requests.get('https://reqres.in/api/users/2')
#    status_code = r.status_code

#    check.equal(status_code, 200, 'статус кода не равен 200')

@allure.feature('Проврка /api/user')
def test__api_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    r = requests.post('https://reqres.in/api/users', data=data)
    status_code = r.status_code

    with allure.step('Проверка статус кода'):
        check.equal(status_code, 201, f'Статус кода не равен 200. Статус код равен {status_code}')

        print(r.json())
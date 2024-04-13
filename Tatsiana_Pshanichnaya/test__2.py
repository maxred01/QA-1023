import requests, pytest, pytest_check as check, allure

@allure.feature('Проверка/api/users')
def test_2_api_status():
    r = requests.get('https://reqres.in/api/users/23')
    status_code = r.status_code

    with allure.step('Проверка статус кода'):
        check.equal(status_code, 404, f'Статус код равен{status_code}')

        print(r.json())
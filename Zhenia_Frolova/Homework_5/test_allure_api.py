import requests
import allure
import pytest_check as check


@allure.feature("Проверка статус кода https://hoster.by/")
def test_api_status_code():
    r = requests.get('https://hoster.by/', timeout=5)
    status_code = r.status_code

    with allure.step("Проверка статус-кода ответа"):
        check.equal(r.status_code, 200, f'Статус код {r.status_code}')

    with allure.step('Проверка url'):
        check.equal(r.url, 'https://hoster.by/')

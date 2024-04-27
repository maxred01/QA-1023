import pytest
import allure
import requests
import pytest_check as check

@allure.feature("Проверка статус кода")
def test_api_status_code():
    respons = requests.get('https://hoster.by/', timeout=13)
    status_code = respons.status_code

    with allure.step('Проверка статус кода'):
        check.equal(respons.status_code, 200, f'Статус код не равен{status_code}')

    with allure.step('Проверка адреса строки'):
        check.equal(respons.url, 'https://hoster.by/')

    with allure.step('Вывод текста в формате json'):
        txt = respons.headers
        allure.attach(txt, name='результат запроса и ответ headers', attachment_type=allure.attachment_type.TEXT)

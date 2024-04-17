import requests
import allure
import pytest_check as check


@allure.feature('Проверка статус кода')
def test_api_user():
    r = requests.get('https://hoster.by/', timeout=10)
    status_code = r.status_code

    with allure.step('Проверка статус кода'):
        check.equal(status_code, 200, f'Статус кода равен {status_code}')

    with allure.step('Проверка URL'):
        check.equal(r.url, 'https://hoster.by/')

    with allure.step('Вывод JSON'):
        txt = r.url
        allure.attach(txt, name='Мой файл результат ответа', attachment_type=allure.attachment_type.TEXT)

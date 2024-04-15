import requests
import pytest_check as check
import allure

@allure.feature('Status code check')
def test_api_status_code():
    url = 'https://hoster.by/'
    r = requests.get(url, timeout = 10)
    status_code = r.status_code

    with allure.step('Step 1 - status code check'):
        check.equal(status_code, 200, f'Status code is not 200. Status code is {status_code}')

    with allure.step('Step 2 - url check'):
        check.equal(r.url, 'https://hoster.by/')

    with allure.step('Step 3 - headers'):
        allure.attach(r.headers, name = 'headers', attachment_type=allure.attachment_type.text)
        some_data = r.headers
        print(some_data)
        
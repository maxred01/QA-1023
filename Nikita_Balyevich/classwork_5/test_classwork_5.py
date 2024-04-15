import allure
import pytest_check as check
import requests


@allure.feature('Check status code')
def test_api_status_code():
    response = requests.get('https://hoster.by/', timeout=10)

    with allure.step('Check status code'):
        check.equal(response.status_code, 200, f'Status code {response.status_code}')

    with allure.step('Check url adr'):
        check.equal(response.url, 'https://hoster.by/')

    # with allure.step('Check url adr'):
    #     print(response.headers)
    #     allure.attach()

'''Homework 5 Example of allure methods'''

import requests
import pytest_check as check
import allure
from bs4 import BeautifulSoup as bs

@allure.feature('Status code check')
@allure.title("Checking availability of https://hoster.by/")
@allure.description("Check of status code and requested url")
@allure.tag("hoster", "status_code", "url_check")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("KP", "QA")
@allure.link("https://hoster.by/", name="Tested Site")
@allure.issue("https://hoster.by/", name="Issue Link")
@allure.testcase("https://hoster.by/", name="TestCase Link")
def test_api_status_code():
    '''Func that tests url for status code and if requested url is correct'''
    url = 'https://hoster.by/'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers, timeout=10)
    status_code = r.status_code

    with allure.step('Step 1 - status code check'):
        check.equal(status_code, 200, f'Status code is not 200. Status code is {status_code}')

    with allure.step('Step 2 - url check'):
        check.equal(r.url, 'https://hoster.by/')

    with allure.step('Step 3 - extract page title'):
        parse_results = bs(r.text, "html.parser")
        title = parse_results.find('title').string
        allure.attach(title, name='title', attachment_type=allure.attachment_type.TEXT)

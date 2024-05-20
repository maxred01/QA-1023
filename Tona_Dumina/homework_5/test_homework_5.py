import requests
import allure
import pytest_check as check
from bs4 import BeautifulSoup as Bs


@allure.title("Testing accessibility  https://hoster.by/ ")
@allure.description("Test check status code, URL and pade title")
@allure.tag("hoster.by", "status_code", "url_check", "title")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "QA")
@allure.link("http://hoster.by/", name="Testing Site")
@allure.issue("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="Issue Link")
@allure.testcase("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="TestCase Link")
def test_hoster_status_code_and_url():
    r = requests.get('https://hoster.by/', timeout=10)

    with allure.step('Check status code'):
        check.equal(r.status_code, 200, f'Status code {r.status_code}')

    with allure.step('Check  URL'):
        check.equal(r.url, 'https://hoster.by/', f' URL = {r.url}')

    with allure.step("Page title output"):
        parse_result = Bs(r.text, "html.parser")
        title = parse_result.find("title").string
        allure.attach(title, name="title", attachment_type=allure.attachment_type.TEXT)

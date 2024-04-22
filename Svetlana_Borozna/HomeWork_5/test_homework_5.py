import requests
import allure
import pytest_check as check
from bs4 import BeautifulSoup as Bs


@allure.title("Тестирование доступности https://hoster.by/ ")
@allure.description("Тест проверяет статус код и URL запрашиваемой страницы")
@allure.tag("hoster.by", "status_code", "url_check", "title")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "QA")
@allure.link("http://hoster.by/", name="TestingSite")
@allure.issue("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="IssueLink")
@allure.testcase("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="TestCaseLink")
def test_hoster_status_code_and_url():
    r = requests.get('https://hoster.by/', timeout=5)

    with allure.step('Проверка статус кода'):
        check.equal(r.status_code, 200, f'Статус код равен {r.status_code}')

    with allure.step('Проверка URL'):
        check.equal(r.url, 'https://hoster.by/', f' URL = {r.url}')

    with allure.step("Вывод title страницы"):
        parse_result = Bs(r.text, "html.parser")
        title = parse_result.find("title").string
        allure.attach(title, name="title", attachment_type=allure.attachment_type.TEXT)

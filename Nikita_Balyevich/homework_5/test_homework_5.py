import requests
import allure
from bs4 import BeautifulSoup as Bs


@allure.title("Testing accessibility https://hoster.by/")
@allure.description("Test check status code, URL and pade title")
@allure.tag("hoster.by", "status_code", "url_check", "title_check")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "QA")
@allure.link("https://hoster.by/", name="Testing_Site")
@allure.issue("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="Issue_Link")
@allure.testcase("https://github.com/maxred01/QA-1023/wiki/HomeWork_5", name="TestCase_Link")
def test_hoster_status_code_url_show_title():
    url = 'https://hoster.by/'
    response = requests.get(url, timeout=10)

    with allure.step("Check status code"):
        assert response.status_code == 200, f'Status code {response.status_code} != 200!'

    with allure.step("Check URL"):
        assert response.url == url, f'Return URL = {response.url}'

    with allure.step("Page title output"):
        parse_result = Bs(response.text, "html.parser")
        title = parse_result.find("title").string
        allure.attach(title, name="title", attachment_type=allure.attachment_type.TEXT)

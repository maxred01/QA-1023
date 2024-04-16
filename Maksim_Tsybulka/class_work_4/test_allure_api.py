import requests
import allure


@allure.title("Тестирование доступности httpbin.org")
@allure.description("Тест проверяет статус код и URL запрашиваемой страницы")
@allure.tag("httpbin", "status_code", "url_check")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "QA")
@allure.link("http://httpbin.org", name="TestingSite")
@allure.issue("https://github.com", name="IssueLink")
@allure.testcase("https://github.com", name="TestCaseLink")
def test_httpbin_status_code_and_url():
    with allure.step("Отправка GET запроса к httpbin.org"):
        response = requests.get("http://httpbin.org/get", timeout=5)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200

    with allure.step("Проверка URL запрашиваемой страницы"):
        assert response.url == "http://httpbin.org/get"

    with allure.step("Вывод title страницы"):
        # В этом примере httpbin.org/get не возвращает HTML с title, поэтому этот шаг не применим.
        # Если бы мы работали с HTML страницей и хотели получить title,
        # нужно было бы использовать парсер, например, BeautifulSoup.
        # Но для данного API мы можем вывести какой-то другой параметр из JSON ответа,
        # например, 'origin'.
        origin = response.json().get('origin')
        allure.dynamic.title(f"Тест доступности httpbin.org с IP {origin}")
        print(f"Origin IP: {origin}")

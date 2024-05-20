from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов хедера на сайте habr.com')
@allure.feature('Проверка главной страницы')
def test_header_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://habr.com/ru/feed/")

    header_elements = [
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[1]'), 'Моя лента'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[2]'), 'Все потоки'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[3]'), 'Разработка'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[4]'),
         'Администрирование'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[5]'), 'Дизайн'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[6]'), 'Менеджмент'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[7]'), 'Маркетинг'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/nav/a[8]'), 'Научпоп')
    ]
    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

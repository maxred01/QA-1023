from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов футера на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://systemofadown.com/")

    footer_elements = [
        (driver.find_element(By.XPATH, '(//footer//a)[1]'), 'HOME'),
        (driver.find_element(By.XPATH, '(//footer//a)[2]'), 'TOUR'),
        (driver.find_element(By.XPATH, '(//footer//a)[3]'), 'MERCH'),
        (driver.find_element(By.XPATH, '(//footer//a)[4]'), 'MUSIC')
    ]
    for elements, elements_text in footer_elements:
        print(elements_text)
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка элементов "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

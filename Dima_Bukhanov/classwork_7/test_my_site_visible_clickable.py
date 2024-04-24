# import time
from selenium import webdriver
from selenium.webdriver.common.keys import By
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://www.audi.by/')

    header_elements = [
        (driver.find_element(By.XPATH, '(//*[@aria-label="Main"]//span)[1]'), 'Модельный ряд'),
        (driver.find_element(By.XPATH, '(//*[@aria-label="Main"]//span)[5]'), 'Покупателям'),
        (driver.find_element(By.XPATH, '(//*[@aria-label="Main"]//span)[9]'), 'Владельцам'),
        (driver.find_element(By.XPATH, '(//*[@aria-label="Main"]//span)[13]'), 'Мир Audi')
    ]
    for elements, elements_text in header_elements:
        print(elements_text)
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            check.is_true(elements.is_displayed)

        with allure.step(f'Проверка элементов "{elements_text}" на отображение на кликабельность'):
            check.is_true(elements.is_enabled)

        with allure.step(f'Проверка текста элементов "{elements_text}" на отображение на кликабельность'):
            check.equal(elements.text, elements_text)

    driver.close()

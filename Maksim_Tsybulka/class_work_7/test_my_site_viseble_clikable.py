from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.cia.gov/")

    header_elements = [
        (driver.find_element(By.ID, 'raa-0'), 'Todays CIA'),
        (driver.find_element(By.ID, 'raa-1'), 'Careers'),
        (driver.find_element(By.ID, 'raa-2'), 'Legacy'),
        (driver.find_element(By.ID, 'raa-3'), 'Newsroom'),
        (driver.find_element(By.ID, 'raa-4'), 'Library')
    ]
    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

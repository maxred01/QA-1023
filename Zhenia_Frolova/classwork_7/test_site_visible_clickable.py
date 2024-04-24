# import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://systemofadown.com/")

    header_elements = [
        (driver.find_element(By.ID, 'menu-item-11'), 'HOME'),
        (driver.find_element(By.ID, 'menu-item-12'), 'TOUR'),
        (driver.find_element(By.ID, 'menu-item-13'), 'MERCH'),
        (driver.find_element(By.ID, 'menu-item-14'), 'MUSIC')
    ]
    for elements, elements_text in header_elements:
        print(elements_text)
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            # assert elements.is_displayed() == True
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка элементов "{elements_text}" на кликабельность'):
            # assert elements.is_enabled() == True
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            # assert elements.is_enabled() == True
            check.equal(elements.text, elements_text)

    driver.close()

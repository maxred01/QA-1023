from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check

@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://hoster.by")

    header_elements = [
        (driver.find_elements(By.ID, 'menu-item')[0].find_element(By.TAG_NAME, 'SPAN'), 'Домены'),
        (driver.find_elements(By.ID, 'menu-item')[7].find_element(By.TAG_NAME, 'SPAN'), 'Хостинг'),
        (driver.find_elements(By.ID, 'menu-item')[22].find_element(By.TAG_NAME, 'SPAN'), 'Облако'),
        (driver.find_elements(By.ID, 'menu-item')[32].find_element(By.TAG_NAME, 'SPAN'), 'Почта'),
        (driver.find_elements(By.ID, 'menu-item')[36].find_element(By.TAG_NAME, 'SPAN'), 'Услуги'),
        (driver.find_elements(By.ID, 'menu-item')[49].find_element(By.TAG_NAME, 'SPAN'), 'IT-аутсорсинг'),
        (driver.find_element(By.CLASS_NAME, 'marked-green'), 'IT-безопасность'),
        (driver.find_element(By.ID, 'menu-item-socnew').find_element(By.TAG_NAME, 'SPAN'), 'SOC'),
        (driver.find_elements(By.ID, 'menu-item')[70].find_element(By.TAG_NAME, 'SPAN'), 'О компании')
    ]
    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

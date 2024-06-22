from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов header на сайте lostfilm.tv')
@allure.feature('Проверка главной страницы')
def test_is_displayed():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lostfilm.tv/")
    header_elements = [
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[1]/span[1]'), 'СЕРИАЛЫ'),
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[2]/span[1]'), 'КИНО'),
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[3]/span[1]'), 'НОВОСТИ'),
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[4]/span[1]'), 'ВИДЕО'),
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[5]/span[1]'), 'НОВИНКИ'),
        (driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[1]/div/a[6]/span[1]'), 'РАСПИСАНИЕ')
    ]

    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    time.sleep(10)

    driver.close()

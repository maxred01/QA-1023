from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов footer на сайте lostfilm.tv')
@allure.feature('Проверка главной страницы')
def test_is_displayed():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lostfilm.tv/")
    footer_elements = [
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[1]'), 'Сериалы'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[2]'), 'Новости'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[3]'), 'Новинки'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[4]'), 'Видео'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[5]'), 'Расписание'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[1]/a[6]'), 'Официальная группа в VK'),
        (driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/a[1]'), 'О проекте'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[2]/a[2]'), 'Правила'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[2]/a[3]'), 'FAQ'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[2]/a[4]'), 'Размещение рекламы'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[2]/a[5]'), 'Обратная связь'),
        (driver.find_element(By.XPATH, '//div[4]/div/div[2]/a[6]'), 'RSS')
    ]

    for elements, elements_text in footer_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    time.sleep(10)

    driver.close()

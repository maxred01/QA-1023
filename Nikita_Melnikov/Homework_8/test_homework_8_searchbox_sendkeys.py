from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


@allure.story('Тесты проверки элемента поиска на сайте lostfilm.tv')
@allure.feature('Проверка главной страницы')
def test_search():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lostfilm.tv/")

    search_box = driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[2]/form/input[1]')
    search_button = driver.find_element(By.XPATH, '//div[3]/div[1]/div/div[2]/form/input[2]')

    search_box.send_keys('во все тяжкие')
    time.sleep(5)
    search_button.click()

    search_elements = [
        (driver.find_element
         (By.XPATH, '//*[@id="left-pane"]/div/div/div[2]/div[2]/a/div[2]/div[1]'), 'ВО ВСЕ ТЯЖКИЕ'),
        (driver.find_element
         (By.XPATH, '//*[@id="left-pane"]/div/div/div[2]/div[4]/a/div[2]/div[1]'), 'EL CAMINO: ВО ВСЕ ТЯЖКИЕ')
    ]

    for elements, elements_text in search_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    time.sleep(10)

    driver.close()

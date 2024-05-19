import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки строки поиска на сайте habr.com')
@allure.feature('Проверка строки поиска')
def test_searchbox():

    driver = webdriver.Chrome()
    driver.fullscreen_window()
    driver.get("https://habr.com/ru/search/")

    search_box = driver.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/form/div/input')
    submit_button = driver.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/form/div/div/span')

    search_box.send_keys('Тестирование')
    time.sleep(2)
    submit_button.click()

    search_results_elements = [
            (driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[1]/div/span[1]/a'),
                                 'ПУБЛИКАЦИИ'),
            (driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[1]/div/span[2]/a'),
                                 'ХАБЫ'),
            (driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[1]/div/span[3]/a'),
                                 'КОМПАНИИ'),
            (driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[1]/div/span[4]/a'),
                                 'ПОЛЬЗОВАТЕЛИ'),
            (driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[1]/div/span[5]/a'),
                                 'КОММЕНТАРИИ')
    ]

    for elements, elements_text in search_results_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()
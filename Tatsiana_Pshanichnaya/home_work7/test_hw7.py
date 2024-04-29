from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')

def test_is_displayed():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.barksfifth.com/")

    header_elements = [
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[1]/a'), 'HOME'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[2]/a'), 'NEW ARRIVALS'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[3]/a'), 'APPAREL'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[4]/a'), 'DESIGNER COLLECTION'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[5]/a'), 'OUTERWEAR'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[6]/a'), 'ACCESSORIES'),
        (driver.find_element(By.XPATH, '//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[7]/a'), 'GIFT CARD'),
        (driver.find_element(By.XPATH,'//*[@id="92683180-6d9d-11ec-b491-437e03cbe2fe"]/ul/li[8]/a'), 'SHOP ALL')
    ]

    footer_elements = [
        (driver.find_element(By.XPATH, '//*[@id="RElidt"]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/nav/ul/li[1]/a'), 'Contact'),
        (driver.find_element(By.XPATH, '//*[@id="RElidt"]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/nav/ul/li[2]/a'), 'Account'),
        (driver.find_element(By.XPATH, '//*[@id="RElidt"]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/nav/ul/li[3]/a'), 'Track my Order'),
        (driver.find_element(By.XPATH, '//*[@id="RElidt"]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/nav/ul/li[4]/a'), 'Privacy Policy'),
        (driver.find_element(By.XPATH, '//*[@id="RElidt"]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/nav/ul/li[5]/a'), 'Size Chart')
    ]

    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    time.sleep(5)

    driver.close()
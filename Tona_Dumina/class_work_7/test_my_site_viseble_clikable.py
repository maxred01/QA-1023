from typing import List, Tuple, Any

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@allure.story('Тесты проверки на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.6pm.com/")

    header_elements = [
        (driver.find_element(By.XPATH, '//a[@href="/shoes"]'), 'SHOES'),
        (driver.find_element(By.XPATH, '(//header//*[contains(text(),"Clothing")])[1]'), 'CLOTHING'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]//a)[63]'), 'BAGS'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]'), 'ACCESSORIES'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]/*[3]/*[5]//*[@origin="www.6pm.com"]'), 'WOMENS'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]/*[3]/*[6]//*[@origin="www.6pm.com"]]'), 'MENS'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]/*[3]/*[7]/*[1]'), 'KIDS'),
        (driver.find_element(By.XPATH, '//*[contains(concat(' ', normalize-space(@class), ' '), " Mh-z ")]//a]'), 'CLEARANCE'),
        (driver.find_element(By.XPATH, '//*[@data-sub-nav="true"]/*[3]/*[9]/*[1]"]'), 'BRANDS'),
    ]
    for elements, elements_text in header_elements:
        print(elements_text)
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            assert elements.is_enabled() == True

        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            assert elements.is_displayed() == True

    driver.close()


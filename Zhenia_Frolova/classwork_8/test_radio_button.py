import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки выбора кнопки')
@allure.feature('Проверка кнопки')
def test_is_clicked():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://demoqa.com/radio-button")

    click_elements = [
        (driver.find_element(By.ID, 'yesRadio'), driver.find_element(By.XPATH,
                                                                     '(//div[@class="custom-control custom-radio '
                                                                     'custom-control-inline"])[1]'), 'Yes')
    ]
    for elements_select, elements_click, elements_text in click_elements:
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            check.is_true(elements_click.is_displayed)

        with allure.step(f'Проверка элементов "{elements_text}" на кликабельность'):
            check.is_true(elements_click.is_enabled())

        with allure.step(f'Выбор кнопки "{elements_text}"'):
            elements_click.click()
            check.is_true(elements_select.is_selected())

            time.sleep(2)

        find_text = driver.find_element(By.XPATH, '//p[@class="mt-3"]').text
        check.is_in(elements_text, find_text)

    driver.close()

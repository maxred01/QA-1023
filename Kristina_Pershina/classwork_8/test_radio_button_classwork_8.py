import time
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.story('Тесты проверки радио-баттона')
@allure.feature('Проверка радио-баттонов')
def test_radio_button():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://demoqa.com/radio-button")

    inputs = [
        ['yesRadio', "(//*[@class='custom-control custom-radio custom-control-inline'])[1]", "Yes"],
        ['impressiveRadio', "(//*[@class='custom-control custom-radio custom-control-inline'])[2]", "Impressive"]
    ]

    for i in inputs:
        radio_button_button = driver.find_element(By.ID, i[0])
        radio_button_field = driver.find_element(By.XPATH, i[1])


        with allure.step(f'Проверка элемента {i[2]} на кликабельность'):
            print(check.is_true(radio_button_button.is_enabled(), f'Radio button {i[2]} is not clickable'))

        with allure.step(f'Проверка элемента {i[2]} на отображение'):
            print(check.is_true(radio_button_field.is_displayed(), f'Radio button {i[2]} is not displayed'))

        with allure.step(f'Проверка, что кнопка {i[2]} выбрана'):
            radio_button_field.click()
            time.sleep(2)
            print(check.is_true(radio_button_button.is_selected(), f'Radio button {i[2]} is not selected'))

    driver.close()

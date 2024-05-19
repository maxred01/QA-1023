import time
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import allure


@allure.story('Тесты проверки радио-баттона на сайте habr.com')
@allure.feature('Проверка радио-баттонов')
def test_radio_buttons():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://habr.com/ru/feed/")

    element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div/button')

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    time.sleep(5)

    radio_buttons = [
        ['uiRussian', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[1]/div/label', "Русский"],
        ['uiEnglish', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[2]/div/label', "English"],
        ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[1]/div/label', "Classic"],
        ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[2]/div/label', "Compact"],
        ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[1]/div/label', "Dark"],
        ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[2]/div/label', "Light"],
        ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[3]/div/label', "System"]
    ]


    for i in radio_buttons:
        try:
            radio_button_button = driver.find_element(By.ID, i[0])
        except NoSuchElementException:
            radio_button_button = driver.find_element(By.NAME, i[0])
        radio_button_field = driver.find_element(By.XPATH, i[1])

        with allure.step(f'Проверка элемента {i[2]} на отображение'):
            check.is_true(radio_button_field.is_displayed(), f'Radio button {i[2]} is not displayed')

        with allure.step(f'Проверка элемента {i[2]} на кликабельность'):
            check.is_true(radio_button_button.is_enabled(), f'Radio button {i[2]} is not clickable')

        with allure.step(f'Проверка, что кнопка {i[2]} выбрана'):
            radio_button_field.click()
            time.sleep(1)
            check.is_true(radio_button_button.is_selected(), f'Radio button {i[2]} is not selected')

    driver.close()

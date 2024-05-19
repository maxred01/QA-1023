import time
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure


@allure.story('Тесты проверки чекбоксов на сайте habr.com')
@allure.feature('Проверка чекбоксов')
def test_checkboxes():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://habr.com/ru/feed/")

    element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div/button')

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    time.sleep(5)

    checkboxes = [
        ['articlesRussian', '//*[@id="overlays"]/div/div[2]/div/div/form/div[3]/div[2]/p[1]/span/span/div/span',
         "Russian"],
        ['articlesEnglish', '//*[@id="overlays"]/div/div[2]/div/div/form/div[3]/div[2]/p[2]/span/span/div/span',
         "English"]
    ]

    for i in checkboxes:
        checkbox_button = driver.find_element(By.ID, i[0])
        checkbox_button_field = driver.find_element(By.XPATH, i[1])

        with allure.step(f'Проверка элемента {i[2]} на отображение'):
            check.is_true(checkbox_button_field.is_displayed(), f'Checkbox {i[2]} is not displayed')
        with allure.step(f'Проверка элемента {i[2]} на кликабельность'):
            check.is_true(checkbox_button.is_enabled(), f'Checkbox {i[2]} is not clickable')

        with allure.step(f'Проверка, что кнопка {i[2]} выбрана'):
            if i[0] == 'articlesRussian':
                checkbox_button_field.click()
                time.sleep(1)
                checkbox_button_field.click()
                time.sleep(1)
            elif i[0] == 'articlesEnglish':
                checkbox_button_field.click()
                time.sleep(1)
            check.is_true(checkbox_button.is_selected(), f'Checkbox {i[2]} is not selected')

    driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest_check as check

USER_NAME = 'Maksim'
USER_EMAIL = 'test_test@gmail.com'
CURRENT_ADDRESS = 'Minsk test'
PERMANENT_ADDRESS = 'Cofix'


@allure.story('Тесты проверки заполнения формы')
@allure.feature('Проверка формы')
def test_is_displayed():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://demoqa.com/text-box")

        form_data = [
            ('userName', USER_NAME),
            ('userEmail', USER_EMAIL),
            ('currentAddress', CURRENT_ADDRESS),
            ('permanentAddress', PERMANENT_ADDRESS)
        ]

        for field_id, value in form_data:
            field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, field_id)))
            with allure.step(f'Проверка элемента "{field_id}" на кликабельность'):
                check.is_true(field_element.is_enabled())

            with allure.step(f'Проверка элемента "{field_id}" на отображение'):
                check.is_true(field_element.is_displayed())

            with allure.step(f'Ввод текста в поле "{field_id}"'):
                field_element.send_keys(value)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
        submit_button.click()

        border = '//div[@class="border col-md-12 col-sm-12"]'
        output_data = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, border)))
        output_text = output_data.text

        check.is_in(USER_NAME, output_text)
        check.is_in(USER_EMAIL, output_text)
        check.is_in(CURRENT_ADDRESS, output_text)
        check.is_in(PERMANENT_ADDRESS, output_text)

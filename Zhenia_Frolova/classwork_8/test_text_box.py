import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки заполнения формы')
@allure.feature('Проверка формы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://demoqa.com/text-box")

    user_name = 'Zhenya'
    user_email = 'qwerty@gmail.com'
    cur_address = 'Minsk'
    perm_addres = 'Brest'

    fill_elements = [
        (driver.find_element(By.ID, 'userName'), 'userName', 'Zhenya'),
        (driver.find_element(By.ID, 'userEmail'), 'userEmail', 'qwerty@gmail.com'),
        (driver.find_element(By.ID, 'currentAddress'), 'currentAddress', 'Minsk'),
        (driver.find_element(By.ID, 'permanentAddress'), 'permanentAddress', 'Brest')
    ]
    for elements, elements_text, fill in fill_elements:
        with allure.step(f'Проверка элементов "{elements_text}" на отображение на экране'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка элементов "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Ввод текста "{elements_text}"'):
            elements.send_keys(fill)

            time.sleep(2)

    driver.find_element(By.ID, 'submit').click()

    find_text = driver.find_element(By.ID, 'output').text
    check.is_true(find_text.find(user_name) != -1)
    check.is_true(find_text.find(user_email) != -1)
    check.is_true(find_text.find(cur_address) != -1)
    check.is_true(find_text.find(perm_addres) != -1)

    driver.close()

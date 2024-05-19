from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://lakikraski.by/")

    header_elements = [
        (driver.find_element(By.XPATH, '((//*[@data-widget_type="ekit-vertical-menu.default"])[1]//a)[1]'),
         'Каталог товаров'),
        (driver.find_element(By.XPATH, '((//*[@data-widget_type="nav-menu.default"])[1]//a)[1]'), 'Бренды'),
        (driver.find_element(By.XPATH, "((//*[@data-widget_type=\"nav-menu.default\"])[1]//"
                                       "*[@aria-haspopup=\"true\"])[1]"), 'В помощь'),
        (driver.find_element(By.XPATH, '((//*[@data-widget_type="nav-menu.default"])[1]//'
                                       '*[@aria-expanded="false"])[5]'), 'Информация'),
        (driver.find_element(By.XPATH, '((//*[@data-widget_type="nav-menu.default"])[1]//'
                                       '*[@aria-expanded="false"])[7]'), 'О компании'),
        (driver.find_element(By.XPATH, '((//*[@data-widget_type="nav-menu.default"])[1]//a)[23]'), 'Контакты')
    ]
    for elements, elements_text in header_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

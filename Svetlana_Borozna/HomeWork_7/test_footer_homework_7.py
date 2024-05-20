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

    footer_elements = [
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[8]'),
         'Архитектурные краски'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[9]'),
         'Промышленные покрытия'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[10]'),
         'Декоративные материалы'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[11]'), 'Инструмент'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[12]'), 'Прочие товары'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[15]'), 'Акции'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[16]'), 'Новости'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[17]'),
         'Оплата и доставка'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[18]'),
         'Дисконтная программа'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[19]'),
         'Публичная оферта'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[20]'),
         'Конфиденциальность'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[21]'), 'Где купить?'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[24]'), 'Системы окраски'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[25]'), 'Вопрос-ответ'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[26]'),
         'Экспертные знания'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[27]'), 'Палитры цветов'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[28]'), 'Брошюры'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[31]'), 'Контакты'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[32]'), 'Реквизиты'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[33]'), 'История'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[34]'), 'Вакансии'),
        (driver.find_element(By.XPATH, '(//*[@data-elementor-type="footer"]/*[2]//span)[35]'), 'Бренды')
    ]
    for elements, elements_text in footer_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

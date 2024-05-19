from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов футера на сайте habr.com')
@allure.feature('Проверка главной страницы')
def test_footer_is_displayed():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://habr.com/ru/feed/")

    footer_elements = [
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/p'), 'Ваш аккаунт'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/ul/li[1]/a'), 'Войти'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/ul/li[2]/a'), 'Регистрация'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/p'), 'Разделы'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[1]/a'), 'Статьи'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[2]/a'), 'Новости'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[3]/a'), 'Хабы'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[4]/a'), 'Компании'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[5]/a'), 'Авторы'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/div/ul/li[6]/a'), 'Песочница'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/p'), 'Информация'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[1]/a'), 'Устройство сайта'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[2]/a'), 'Для авторов'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[3]/a'), 'Для компаний'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[4]/a'), 'Документы'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[5]/a'), 'Соглашение'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[3]/div/ul/li[6]/a'),
         'Конфиденциальность'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/p'), 'Услуги'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/div/ul/li[1]/a'),
         'Корпоративный блог'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/div/ul/li[2]/a'), 'Медийная реклама'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/div/ul/li[3]/a'),
         'Нативные проекты'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/div/ul/li[4]/a'),
         'Образовательные программы'),
        (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/div/ul/li[5]/a'), 'Стартапам')
    ]
    for elements, elements_text in footer_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

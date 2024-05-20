from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


@allure.story('Тесты проверки элементов на сайте')
@allure.feature('Проверка главной страницы')
def test_is_displayed():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://hoster.by/")

    header_footer_elements = [
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[1]'), 'Домены'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[8]'), 'Хостинг'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[23]'), 'Облако'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[33]'), 'Почта'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[37]'), 'Услуги'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[50]'), 'IT-аутсорсинг'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[60]'), 'IT-безопасность'),
        (driver.find_element(By.XPATH, '//*[@id="menu-item-socnew"]'), 'SOC'),
        (driver.find_element(By.XPATH, '(//*[@id="menu-item"])[71]'), 'О компании'),
        (driver.find_element(By.XPATH, '//*[@id="menu_auth"]/div'), 'Войти'),
        (driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[4]/div[2]/div[1]'), 'Контакты'),
        # (driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[4]/div[3]/div'), '')
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-domains"]'), 'Регистрация доменов'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-service-cloud"]'), 'Облачная инфраструктура'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-hosting-unix"]'), 'Хостинг сайтов'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-hosting-personalnye-dannye"]'),
         'Хостинг персональных данных'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-solutions-ssl"]'), 'SSL-сертификаты'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-solutions-informatsionnaya-bezopasnost"]'),
         'Информационная безопасность'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-solutions-email"]'), 'Почта'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-cloud-scloud"]'), 'Облако sCloud'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-cloud-server"]'), 'Облачный VPS'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-solutions-administration"]'), 'IT-аутсорсинг'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-pers_data"]'),
         'Политика в отношении обработки персональных данных'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-cookie"]'),
         'Политика в отношении обработки файлов cookie'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-cookie-settings"]'), 'Настройка файлов cookie'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-video"]'), 'Политика видеонаблюдения'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-clients-doc-pub"]'), 'Договоры'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-help"]'), 'FAQ'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-clients-payments"]'), 'Способы оплаты'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-clients-career"]'), 'Карьера'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-clients-cases"]'), 'Кейсы'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-actions-develop"]'), 'Разработка сайтов'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-actions-seo"]'), 'Продвижение сайтов'),
        (driver.find_element(By.XPATH, '//*[@id="footer-menu-solutions-partners"]'), 'Стать партнером'),
        (driver.find_element(By.XPATH, '//*[@id="footer-link-contacts"]'), 'Все контакты'),
        (driver.find_element(By.XPATH, '//*[@id="footer-link-mailto"]'), 'Написать письмо'),
        # (driver.find_element(By.XPATH, '(//*[@alt="twitter"])[4]'), ''),
        # (driver.find_element(By.XPATH, '(//*[@alt="facebook"])[4]'), ''),
        # (driver.find_element(By.XPATH, '(//*[@alt="vk"])[4]'), ''),
        # (driver.find_element(By.XPATH, '//*[@alt="instagram"]'), ''),
        # (driver.find_element(By.XPATH, '(//*[@alt="telegram"])[4]'), ''),
        # (driver.find_element(By.XPATH, '//*[@alt="youtube"]'), '')
    ]

    for elements, elements_text in header_footer_elements:
        with allure.step(f'Проверка элемента "{elements_text}" на кликабельность'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Проверка элемента "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Проверка текста элемента "{elements_text}"'):
            check.equal(elements.text, elements_text)

    time.sleep(30)

    driver.close()

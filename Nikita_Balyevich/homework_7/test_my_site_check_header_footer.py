from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest_check as check


@allure.story('Tests for checking elements on the site')
@allure.feature('Checking the home page')
def test_is_displayed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://manjaro.org/")

    header_footer_elements = [
        (driver.find_element(By.XPATH, '(//*[@id="desktop-menu"]//a)[1]'), 'Merchandise'),
        (driver.find_element(By.XPATH, '(//*[@id="desktop-menu"]//a)[2]'), 'Hardware'),
        (driver.find_element(By.XPATH, '(//*[@id="desktop-menu"]//a)[3]'), 'Contact'),
        (driver.find_element(By.XPATH, '(//*[@id="desktop-menu"]//a)[4]'), 'Download'),
        (driver.find_element(By.XPATH, '(//*[@id="left-menu"]//button)[1]'), 'Project'),
        (driver.find_element(By.XPATH, '(//*[@id="left-menu"]//button)[2]'), 'Explore'),
        (driver.find_element(By.XPATH, '(//*[@id="left-menu"]//button)[3]'), 'Learn'),
        (driver.find_element(By.XPATH, '(//*[@id="left-menu"]//button)[4]'), 'Supporters'),
        # (driver.find_element(By.ID, '[id="donate-btn"]'), 'Donate'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Privacy Policy"]'), 'Privacy Policy'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Terms of use"]'), 'Terms Of Use'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Imprint"]'), 'Imprint'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Facebook"]'), 'Facebook'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Youtube"]'), 'Youtube'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Twitter"]'), 'Twitter'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Code of Conduct"]'), 'Code Of Conduct'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Source Code"]'), 'Source Code'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Sending a PR"]'), 'Sending A PR'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Development"]'), 'Development'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Packages"]'), 'Packages'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Security"]'), 'Security'),
        (driver.find_element(By.XPATH, '//*[@aria-label="General"]'), 'General'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Testing"]'), 'Testing'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Mirrors"]'), 'Mirrors'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Log in"]'), 'log in')
    ]
    for elements, elements_text in header_footer_elements:
        with allure.step(f'Checking the element "{elements_text}" for clickability'):
            check.is_true(elements.is_enabled())

        with allure.step(f'Checking element "{elements_text}" for display'):
            check.is_true(elements.is_displayed())

        with allure.step(f'Checking element text "{elements_text}"'):
            check.equal(elements.text, elements_text)

    driver.close()

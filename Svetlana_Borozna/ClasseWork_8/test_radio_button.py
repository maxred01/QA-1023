import time
from pytest_check import check
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button():
    driver = webdriver.Chrome()

    driver.get('https://demoqa.com/radio-button')

    yes_button = driver.find_element(By.XPATH,
                                     "(//*[contains(concat(' ', normalize-space(@class), ' '), "
                                     "' custom-control ')])[1]")

    yes_button.click()
    check.is_true(yes_button.is_selected())

    find_text = driver.find_element(By.CLASS_NAME, 'mt-3')
    check.is_in('Yes', find_text)

    time.sleep(3)

    driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_forma():
    driver = webdriver.Chrome()

    driver.get('https://demoqa.com/text-box')
    forma_elements = [
        (driver.find_element(By.XPATH, '//*[@placeholder="Full Name"]'), 'name', 'Penguin'),
        (driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]'), 'email', 'penguin@gmail.com'),
        (driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]'), 'cur_address', 'penguiniya'),
        (driver.find_element(By.XPATH, '//*[@id="permanentAddress"]'), 'per_addres', 'Guinpen')
    ]

    submit_button = driver.find_element(By.XPATH, '//form//button')

    for elements, text, my in forma_elements:
        elements.send_keys(my)

    submit_button.send_keys(Keys.ENTER)

    time.sleep(3)

    driver.close()

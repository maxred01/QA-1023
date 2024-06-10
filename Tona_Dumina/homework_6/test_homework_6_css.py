import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://hoster.by/service/domains/')

driver.find_element(By.CSS_SELECTOR, ' [id="accept"]').click()

input_search_box = driver.find_element(By.CSS_SELECTOR, ' [name="domain_name"]')

input_search_button = driver.find_element(By.CSS_SELECTOR, ' [id="domain"]')


input_search_box.send_keys("luxsystems.by")
time.sleep(2)
input_search_button.click()
time.sleep(2)

input_search_button.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()
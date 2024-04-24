from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.21vek.by')

input_search_box = driver.find_element(By.XPATH, '//*[@aria-label="search"]')

input_search_box.send_keys("Selenium Python")

input_search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_size(800, 600)

driver.get("https://www.google.com")

input_search_box = driver.find_element(By.NAME, "q")

input_search_box.send_keys("Selenium Python")

input_search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()

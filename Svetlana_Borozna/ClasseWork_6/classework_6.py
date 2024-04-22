from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://lakikraski.by/')

driver.maximize_window()

time.sleep(2)

search_box = driver.find_element(By.XPATH, "(//*[contains(concat(' ', normalize-space(@class), ' '), ' probox ')])[1]//input[@type='search']")

search_box.send_keys("Biora 3")
time.sleep(5)
#search_box.send_keys(Keys.ENTER)

time.sleep(5)

driver.close()
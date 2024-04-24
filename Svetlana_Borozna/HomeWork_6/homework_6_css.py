import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://hoster.by/service/domains/')

search_box = driver.find_element(By.CSS_SELECTOR, ' [name="domain_name"]')

search_button = driver.find_element(By.CSS_SELECTOR, ' [id="domain"]')

search_box.send_keys("Penguins.by")

search_button.send_keys(Keys.ENTER)

time.sleep(5)

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.set_window_size(1920,1080)

driver.get('https://hoster.by/service/domains/')

input_search_box = driver.find_element(By.XPATH, '//section//form//*[@name="domain_name"]')
input_search_box.send_keys('archlinux.by')
input_search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()

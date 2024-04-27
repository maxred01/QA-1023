import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.set_window_size(1920, 1080)

driver.get("https://aur.archlinux.org/")

input_search_box = driver.find_element(By.ID, "pkgsearch-field")

input_search_box.send_keys("selenium")

input_search_box.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()

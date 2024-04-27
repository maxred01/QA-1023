import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.onliner.by/")

input_search_box = driver.find_element(By.XPATH, '//*[@id="fast-search"]/form/input[1]')


input_search_box.send_keys('iphone')

time.sleep(10)
driver.quit()

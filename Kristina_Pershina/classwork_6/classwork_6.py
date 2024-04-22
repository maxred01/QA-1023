from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://etherscan.io/")

search_box = driver.find_element(By.ID, "search-panel")
submit_button = driver.find_element(By.XPATH, '//*[@id="content"]/section[1]/div/div/div[1]/form/div/div[3]/button')

search_box.send_keys('19712631')
submit_button.click()

time.sleep(5)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_size(1920,1080)

driver.get("https://fintech.tinkoff.ru/start/")

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/h3/button/span/span')

search_box.send_keys("Selenium Python")

search_box.send_keys(Keys.ENTER)

time.sleep(5)

driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.kufar.by/l/r~minsk")

input_search_box = driver.find_element(By.XPATH, '//*[@placeholder="Искать объявления"]')

input_search_box.send_keys("Квартира")

input_search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()

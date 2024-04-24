import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.set_window_size(1600, 800)

driver.get('https://hoster.by/service/domains/')

input_search_box = (driver.find_element
                    (By.XPATH, '//section//*[@name="domain_name"]'))

input_search_box.send_keys('https://nikitamelnikov.by')

input_search_button = (driver.find_element
                       (By.XPATH, '//*[@id="domain"]'))

input_search_button.click()

time.sleep(5)

driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://etherscan.io/")
# driver.get("https://etherscan.io/tx/0xc3187a490bf370a984efd8b23b66de923a6a7d19241278d0cba170a2595b10c2/")

search_box = driver.find_element(By.ID, "search-panel")
submit_button = driver.find_element(By.XPATH, '//*[@id="content"]/section[1]/div/div/div[1]/form/div/div[3]/button')
#
search_box.send_keys('0xc3187a490bf370a984efd8b23b66de923a6a7d19241278d0cba170a2595b10c2')
time.sleep(2)
submit_button.click()

token = driver.find_element(By.CSS_SELECTOR, "a[target='_parent'][data-bs-trigger='hover']")
print(token.text)

time.sleep(5)

driver.quit()

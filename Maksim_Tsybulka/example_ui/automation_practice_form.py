import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoQaFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://demoqa.com/automation-practice-form")

    def test_fill_form(self):
        driver = self.driver

        first_name = "John"
        first_name_field = driver.find_element(By.ID, "firstName")
        first_name_field.send_keys(first_name)

        last_name = "Doe"
        last_name_field = driver.find_element(By.ID, "lastName")
        last_name_field.send_keys(last_name)

        email = "johndoe@example.com"
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys(email)

        gender_button = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
        gender_button.click()

        phone_number = "1234567890"
        phone_number_field = driver.find_element(By.ID, "userNumber")
        phone_number_field.send_keys(phone_number)

        birthdate_field = driver.find_element(By.ID, "dateOfBirthInput")
        birthdate_field.send_keys("01 Jan 1990")
        birthdate_field.send_keys(Keys.ENTER)

        subjects_input = driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Maths")
        subjects_input.send_keys(Keys.ENTER)
        subjects_input.send_keys("English")
        subjects_input.send_keys(Keys.ENTER)

        hobbies_checkbox = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
        hobbies_checkbox.click()

        address = "123 Main Street, New York"
        address_field = driver.find_element(By.ID, "currentAddress")
        address_field.send_keys(address)

        state_dropdown = driver.find_element(By.ID, "state")
        state_dropdown.click()
        state_option = driver.find_element(By.XPATH, '//div[contains(@class, "menu")]/div[contains(text(), "NCR")]')
        state_option.click()

        city_dropdown = driver.find_element(By.ID, "city")
        city_dropdown.click()
        city_option = driver.find_element(By.XPATH, '//div[contains(@class, "menu")]/div[contains(text(), "Delhi")]')
        city_option.click()

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))

        result_name = driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[2]').text
        self.assertEqual(f"{first_name} {last_name}", result_name)

        result_email = driver.find_element(By.XPATH, '//table/tbody/tr[2]/td[2]').text
        self.assertEqual(email, result_email)

        result_phone = driver.find_element(By.XPATH, '//table/tbody/tr[4]/td[2]').text
        self.assertEqual(phone_number, result_phone)

        result_address = driver.find_element(By.XPATH, '//table/tbody/tr[6]/td[2]').text
        self.assertEqual(address, result_address)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

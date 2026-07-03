from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the chrome driver
driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com"
driver.get(URL)

# AUTOCOMPLETE
autocomplete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Autocomplete']")
    )
)
autocomplete_button.click()
assert "autocomplete" in driver.current_url

# 1. Address Label (Verification)
address_label = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[@for='autocomplete']"))
)
print(f"Bhetiyeko text: {address_label.text}")

# 2. Address Input Box
address_field = driver.find_element(By.XPATH, "//input[@id='autocomplete']")
address_field.send_keys("Fasku")

# 3. Street address
street_num_field = driver.find_element(By.XPATH, "//input[@id='street_number']")
street_num_field.send_keys("Suite 400")

# 4. Street address 2
route_field = driver.find_element(By.XPATH, "//input[@id='route']")
route_field.send_keys("Nagarjun-6")

# 5. City
city_field = driver.find_element(By.XPATH, "//input[@id='locality']")
city_field.send_keys("kathmandu")

# 6. State
state_field = driver.find_element(By.XPATH, "//input[@id='administrative_area_level_1']")
state_field.send_keys("NY")

# 7. Zip code
zip_field = driver.find_element(By.XPATH, "//input[@id='postal_code']")
zip_field.send_keys("10001")

# 8. Country
country_field = driver.find_element(By.XPATH, "//input[@id='country']")
country_field.send_keys("Nepal")


time.sleep(3) 


driver.back()


assert driver.current_url == URL or driver.current_url == URL + "/"





time.sleep(10)

driver.quit()
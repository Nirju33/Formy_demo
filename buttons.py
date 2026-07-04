from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the chrome driver
driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)


buttons_button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-lg'][normalize-space()='Buttons']"))
)
buttons_button.click()

time.sleep(2)
assert "buttons" in driver.current_url

primary_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Primary']"))
)
primary_btn.click()

time.sleep(1) 


success_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Success']")
success_btn.click()

time.sleep(1)

danger_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Danger']")
danger_btn.click()

time.sleep(2)


driver.back()

assert driver.current_url == URL or driver.current_url == URL + "buttons"


time.sleep(2)
driver.quit()
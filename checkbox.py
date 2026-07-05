from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

Checkbox_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Checkbox']"))
)
Checkbox_button.click()
WebDriverWait(driver, 10).until(EC.url_contains("checkbox"))

checkbox1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkbox-1"))
)
checkbox1.click()

time.sleep(1)


checkbox2 = driver.find_element(By.XPATH, "//input[@id='checkbox-2']")
checkbox2.click()

time.sleep(1)


checkbox3 = driver.find_element(By.XPATH, "//input[@id='checkbox-3']")
checkbox3.click()

time.sleep(2)


driver.back()


assert driver.current_url == URL or driver.current_url == URL + "checkbox"

time.sleep(7)


driver.quit()
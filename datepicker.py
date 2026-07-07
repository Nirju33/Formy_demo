from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

URL = "https://formy-project.herokuapp.com/"
driver.get(URL)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Datepicker']"))
).click()

WebDriverWait(driver, 10).until(EC.url_contains("datepicker"))
assert "datepicker" in driver.current_url

datepicker_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='datepicker']"))
)
datepicker_input.click()
time.sleep(1.5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//th[@class='datepicker-switch'])[1]"))
).click()
time.sleep(1.5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//th[@class='datepicker-switch'])[2]"))
).click()
time.sleep(1.5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'year') and text()='2026']"))
).click()
time.sleep(1.5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'month') and text()='Jun']"))
).click()
time.sleep(1.5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//td[@class='day' and text()='25'])[1]"))
).click()

time.sleep(5)
driver.quit()
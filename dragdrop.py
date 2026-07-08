from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()


URL = "https://formy-project.herokuapp.com/"
driver.get(URL)


DragDrop_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Drag and Drop']"))
).click()

WebDriverWait(driver, 10).until(EC.url_contains("dragdrop"))

time.sleep(5)
driver.quit()


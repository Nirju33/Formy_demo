from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_key_and_mouse_press():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/keypress")
    time.sleep(2)
    
    try:
        driver.find_element(By.ID, "name").send_keys("Nirjala")
        time.sleep(1)
        
        driver.find_element(By.ID, "button").click()
    
        time.sleep(2)

        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_key_and_mouse_press()
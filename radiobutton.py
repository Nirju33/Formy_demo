from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_radio_button():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://formy-project.herokuapp.com/")
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, 
            "//a[@class='btn btn-lg'][normalize-space()='Radio Button']"))
        ).click()
    
        radio_1 = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='radio-button-1']"))
        )
        radio_1.click()
        time.sleep(1)
        
        radio_2 = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='option2']"))
          
        )
        radio_2.click()
        time.sleep(2)
        
        radio_3 = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//input[@value='option3']"))
            
        )
        radio_3.click()
        time.sleep(3)
        
       
        assert "radiobutton" in driver.current_url
     

        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_radio_button()
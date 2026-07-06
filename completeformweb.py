from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def test_complete_web_form():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(2)
    
    try:
        driver.find_element(By.ID, "first-name").send_keys("Nirjala")
        driver.find_element(By.ID, "last-name").send_keys("QA")
        driver.find_element(By.ID, "job-title").send_keys("Automation Engineer")
        driver.find_element(By.ID, "radio-button-2").click()
        driver.find_element(By.ID, "checkbox-2").click()
        
        Select(driver.find_element(By.XPATH, "//select[@id='select-menu']")).select_by_value("")
        driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("06/23/2026" + Keys.ENTER)
        time.sleep(5)
        
        driver.find_element(By.XPATH, "//a[normalize-space()='Submit']").click()
        time.sleep(2)
        
    except Exception:
        pass
    finally:
        driver.quit()

if __name__ == "__main__":
    test_complete_web_form()
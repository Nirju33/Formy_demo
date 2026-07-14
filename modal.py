
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_modal():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='Modal']").click()
        time.sleep(2)

        driver.find_element(By.ID, "modal-button").click()
        time.sleep(1)

        driver.find_element(By.ID, "close-button").click()
        time.sleep(2)
        
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_modal()
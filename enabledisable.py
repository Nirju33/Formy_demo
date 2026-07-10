from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_enable_disable():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    time.sleep(2)

    try:
        driver.find_element(By.XPATH,
            "//a[@class='btn btn-lg'][normalize-space()='Enabled and disabled elements']").click()
        time.sleep(2)

        disabled_input = driver.find_element(By.ID, "disabledInput")
  
        driver.find_element(By.ID, "input").send_keys("Testing enabled field")
        time.sleep(2)
        
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_enable_disable()
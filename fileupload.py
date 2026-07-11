from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main_page(driver):
    form_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-lg'][normalize-space()='File Upload']"))
    )
    form_button.click()
    time.sleep(2)


def file_upload(driver):
    file_pick = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload-field"))
    )
    file_path = r"C:\Users\NIRJALA\Downloads\four.png"
    file_pick.send_keys(file_path)
    time.sleep(5)


def reset_page(driver):
    reset_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset']"))
    )
    reset_btn.click()
    time.sleep(3)


def main():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/")
    driver.maximize_window()
    
    try:
        main_page(driver)
        file_upload(driver)
        reset_page(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
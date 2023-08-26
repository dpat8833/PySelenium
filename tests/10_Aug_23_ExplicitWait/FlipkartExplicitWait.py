import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com")
    driver.maximize_window()

    close_popup_btn = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))))
    close_popup_btn.click()
    driver.implicitly_wait(5)
    driver.quit()

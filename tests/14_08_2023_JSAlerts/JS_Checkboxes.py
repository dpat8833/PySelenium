import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_JSCheckBoxes():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
    checkbox.click()
    for c in checkboxes:
        if not c.is_selected():
            c.click()
            time.sleep(10)


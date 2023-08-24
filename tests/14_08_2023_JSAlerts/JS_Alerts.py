import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_JSAlerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    # JS_Alert_Btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    # JS_Alert_Btn.click()
    JS_Prompt = driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
    JS_Prompt.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Dibyajyoti")
    alert.accept()
    result = driver.find_element(By.ID, "result")
    print(result.text)


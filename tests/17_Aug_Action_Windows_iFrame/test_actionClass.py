import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_actionClass():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    first_name = driver.find_element(By.NAME, "firstname")
    # For creating an action class, we have to create an object of action class
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "dibyajyoti").key_up(Keys.SHIFT).perform()
    last_name = driver.find_element(By.NAME, "lastname")
    actions.key_down(Keys.SHIFT).send_keys_to_element(last_name, "pattnaik").key_up(Keys.SHIFT).perform()
    url = driver.find_element(By.XPATH, "//a[contains(text(),'Click here to Download File')]")
    # actions.context_click(url).perform()

    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Selenium").perform()
    time.sleep(20)

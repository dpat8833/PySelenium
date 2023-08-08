import logging

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_login_to_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    time.sleep(10)
    driver.find_element(By.ID, "login-username").send_keys("pattnaikdibyajyoti69@gmail.com")
    driver.find_element(By.ID, "login-password").send_keys("Djpsd@25241")
    driver.find_element(By.ID, "js-login-btn").click()
    time.sleep(10)
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("The title is " + driver.title)
    driver.find_element(By.CLASS_NAME, "icon-button").click()
    time.sleep(2)
    # driver.find_element(By.CLASS_NAME, "dropdown-menu-list-item").click()
    driver.find_element(By.XPATH, "(//li[contains(text(),'Logout')])[2]").click()

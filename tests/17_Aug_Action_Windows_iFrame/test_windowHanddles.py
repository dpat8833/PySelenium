import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_window_handles():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    parent_window = driver.current_window_handle
    print(parent_window)
    click_here = driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]")
    click_here.click()
    window_handles = driver.window_handles
    print(window_handles)
    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Found the text")
            break
    driver.switch_to.window(parent_window)
    time.sleep(10)
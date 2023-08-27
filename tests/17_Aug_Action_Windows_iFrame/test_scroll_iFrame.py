import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_actionClass():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    driver.maximize_window()
    iFrame = driver.find_element(By.NAME, "nested_scrolling_frame")
    scroll_origin = ScrollOrigin.from_element(iFrame)
    actions = ActionChains(driver)
    actions.scroll_from_origin(scroll_origin, 0, 100).perform()
    time.sleep(100)

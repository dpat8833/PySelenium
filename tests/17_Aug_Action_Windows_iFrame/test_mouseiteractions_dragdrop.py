import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_actionClass():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()
    clickable_link = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
    # actions.click_and_hold(clickable_link).key_down(Keys.SHIFT).send_keys("dibyajyoti").key_up(Keys.SHIFT).perform()
    actions.key_down(Keys.SHIFT).send_keys_to_element(clickable_link, "dibyajyoti").key_up(Keys.SHIFT).perform()
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    # actions.click_and_hold(source).move_to_element(target).release().perform()
    actions.drag_and_drop(source, target).perform()
    drop_status = driver.find_element(By.ID, "drop-status")
    print(drop_status.text)
    time.sleep(10)

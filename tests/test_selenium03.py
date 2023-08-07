import pytest
from selenium import webdriver
import logging


# Chrome Options
def test_login():
    chrome_options = webdriver.ChromeOptions()
    extension_path = "/Users/pattn/Downloads/adBlocker.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)
    chrome_options.add_argument("--head=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.flipkart.com")
    # driver.maximize_window()

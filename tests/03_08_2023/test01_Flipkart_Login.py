import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_browser():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com")
    time.sleep(10)
    driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("The title is" + driver.title)
    assert "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!" in driver.title
    print("Clicked the ✕ button")


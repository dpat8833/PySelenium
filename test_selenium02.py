import pytest
from selenium import webdriver
import logging


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver


def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://www.makemytrip.com")
    print("The title of mmt is " + driver.title)
    LOGGER.info("This is information logs")
    LOGGER.error("This is a error log")
    LOGGER.critical("This is a critical log")
    LOGGER.warning("This is a warning log")
    # Verification is done at this step. Actual result == expected result
    assert "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday" == driver.title
    print("The URL of mmt is " + driver.current_url)

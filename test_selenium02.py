import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver


def test_ope_url_verify_title(driver):
    driver.get("https://www.makemytrip.com")
    print("The title of mmt is " + driver.title)
    # Verification is done at this step. Actual result == expected result
    assert "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday" == driver.title
    print("The URL of mmt is " + driver.current_url)


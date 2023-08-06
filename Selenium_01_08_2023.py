# call selenium
# use the selenium commands

# Selenium code(Python/Java) -> HTTP Requests ->ChromeDriver/GeckoDriver->Chrome/Firefox

from selenium import webdriver

# Create a session and send the commands

browser = webdriver.Chrome()
browser.get("https://makemytrip.com")

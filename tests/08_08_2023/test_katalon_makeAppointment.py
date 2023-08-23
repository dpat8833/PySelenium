import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_katalon_makeAppointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    # time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "btn-make-appointment").click()
    # time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    # time.sleep(5)
    driver.implicitly_wait(5)
    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Seoul CURA Healthcare Center")
    # time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    healthcare_program = driver.find_element(By.ID, "radio_program_medicaid")
    healthcare_program.click()
    date_picker = driver.find_element(By.ID, "txt_visit_date")
    date_picker.send_keys("18/08/2023")
    comment = driver.find_element(By.ID, "txt_comment")
    comment.send_keys("Please book my appointment")
    book_appointment = driver.find_element(By.XPATH, "//button[text()='Book Appointment']")
    book_appointment.click()
    # time.sleep(5)
    driver.implicitly_wait(5)


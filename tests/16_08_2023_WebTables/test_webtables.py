import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_WebTables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    # driver.maximize_window()
    #
    # # While automating a web table first we need to identify how many rows and columns are present in the table.
    # # row-count-xpath - //table[@id='customers']/tbody/tr
    # # column-count-xpath - //table[@id='customers']/tbody/tr[2]/td

    # row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    # row_count = len(row_elements)
    # print("Total number of rows in the table", row_count)
    #
    # column_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    # column_count = len(column_elements)
    # print("Total number of columns in the table", column_count)
    #
    # first_part = "//table[@id='customers']/tbody/tr["
    # second_part = "]/td["
    # third_part = "]"
    #
    # for i in range(2, row_count + 1):
    #     for j in range(1, column_count + 1):
    #         dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
    #         print(dynamic_path)
    #         data = driver.find_element(By.XPATH, dynamic_path).text
    #         if "Helen Bennett" in data:
    #             country_path = f"{dynamic_path}/following-sibling::td"
    #             country_text = driver.find_element(By.XPATH, country_path).text
    #             print(f"Helen Bennett is in {country_text}")
    #
    #             driver.get("https://awesomeqa.com/webtable1.html")
    # table = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody")
    table_row = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody/tr")
    # find element chaining
    # table_row = table.find_elements(By.TAG_NAME, "tr")
    for row in table_row:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)

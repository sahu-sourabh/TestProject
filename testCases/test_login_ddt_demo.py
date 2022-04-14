from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities import ExcelUtils


def test_login_ddt_demo():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://www.saucedemo.com/")

    rows = ExcelUtils.getRowCount("TestData/loginData1.xlsx", "Sheet1")
    print("No of Rows: ", rows)

    for row in range(2, rows):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")

        username = ExcelUtils.readData("TestData/loginData1.xlsx", "Sheet1", row, 1)
        password = ExcelUtils.readData("TestData/loginData1.xlsx", "Sheet1", row, 2)

        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        # time.sleep(5)

        actual_URL = driver.current_url
        expected_URL = "https://www.saucedemo.com/inventory.html"

        if actual_URL == expected_URL:
            print("********** Login Successful **********")
            WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "logout_sidebar_link")))
            driver.find_element(By.ID, "logout_sidebar_link").click()
            driver.quit()
        else:
            print("********** Login Failed **********")
            driver.quit()

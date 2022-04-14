from selenium import webdriver
from selenium.webdriver.common.by import By

# 3.1 of Documentation

class LoginPage:
    # Locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    # Constructor - for initializing the driver
    def __init__(self, driver): # this 'driver' will come from actual testcase
        self.driver = driver # this 'driver' we will initialize to our local driver(class driver)

    # Action Methods
    def setUserName(self, username): # this username will come from actual testcase
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password): # this username will come from actual testcase
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

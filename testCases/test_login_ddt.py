import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

# 3.2 of Documentation


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicaionURL()
    path = "TestData/LoginData.xlsx"

    logger = LogGen.loggen1()

    @pytest.mark.regression
    def test_login_ddt(self, setUpFixture):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Validation Login DDT Test **********")
        # self.driver = setUpFixture
        # self.driver.get(self.baseURL)
        # self.logger.info("********** Navigated to baseURL **********")
        # # self.driver.maximize_window()
        #
        # # creating object of class LoginPage and passing driver reference in the constructor
        # self.lp = LoginPage(self.driver)
        # self.logger.info("********** Received driver reference in LoginPage(self.driver) **********")

        # Reading number of Rows from ExcelUtils.py
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows: ", self.rows)

        list_status = []        # empty list Variable

        for row in range(2, self.rows+1):
            self.logger.info("********** Inside For Loop **********")

            self.driver = setUpFixture
            self.logger.info("********** setUpFixture **********")
            self.driver.delete_all_cookies()
            self.driver.get(self.baseURL)
            self.logger.info("********** Navigated to baseURL **********")
            # self.driver.maximize_window()

            # creating object of class LoginPage and passing driver reference in the constructor
            self.lp = LoginPage(self.driver)
            self.logger.info("********** Received driver reference in LoginPage(self.driver) **********")

            # Get Data
            self.username = ExcelUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', row, 2)
            self.expected = ExcelUtils.readData(self.path, 'Sheet1', row, 3)

            print("username: ", self.username)
            print("password: ", self.password)
            print("expected: ", self.expected)

            self.logger.info("********** Got Data **********")
            # Set Data
            self.lp.setUserName(self.username)
            self.logger.info("********** Entered Username **********")
            self.lp.setPassword(self.password)
            self.logger.info("********** Entered Password **********")
            self.lp.clickLogin()
            self.logger.info("********** Clicked Login Button **********")

            # time.sleep(5)

            actual_title = self.driver.title
            self.logger.info("********** Captured actual_title **********")
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected == "Pass":
                    self.logger.info("********** Inside if-if **********")
                    self.logger.info("********** Passed **********")
                    # self.lp.clickLogout()
                    list_status.append("Pass")
                    # self.driver.quit()
                    self.logger.info("********** Inside if-if self.driver.quit() **********")
                elif self.expected == "Fail":
                    self.logger.info("********** Inside if-elif **********")
                    self.logger.info("********** Failed **********")
                    # self.lp.clickLogout()
                    list_status.append("Fail")
                    # self.driver.quit()
                    self.logger.info("********** Inside if-elif self.driver.quit() **********")
            elif actual_title != expected_title:
                if self.expected == "Pass":
                    self.logger.info("********** Inside elif-if **********")
                    self.logger.info("********** Failed **********")
                    list_status.append("Fail")
                    # self.driver.quit()
                    self.logger.info("********** Inside elif-if self.driver.quit() **********")
                elif self.expected == "Fail":
                    self.logger.info("********** Inside elif-elif **********")
                    self.logger.info("********** Passed **********")
                    list_status.append("Pass")
                    # self.driver.quit()
                    self.logger.info("********** Inside elif-elif self.driver.quit() **********")

        print("list_status", list_status)

        if "Fail" not in list_status:
            self.logger.info("********** Login DDT Test Passed **********")
            # self.driver.quit()
            assert True
        else:
            self.logger.error("********** Login DDT Test Failed **********")
            # self.driver.quit()
            assert False

        self.logger.info("********** End Of Login DDT Test **********")
        self.logger.info("********** Completed Test_002_DDT_Login **********")
        self.driver.quit()

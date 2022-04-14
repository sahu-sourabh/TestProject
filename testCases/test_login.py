import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# 3.2 of Documentation


# Test Class
class Test_001_Login:   # class name with test case id

    # Test Common Variables
    # Pre-requisite Data for every Test

    # Static Data/Hard coded Data
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    # Dynamic Data - 5.3 of Documentation
    baseURL = ReadConfig.getApplicaionURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # Logger Object
    # logger = LogGen.loggen()      # Not Working
    logger = LogGen.loggen1()       # Working

    # Test Methods
    @pytest.mark.regression
    def test_homePageTitle(self, setUpFixture):
        self.logger.info("********** Test_001_Login **********")
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = setUpFixture
        self.driver.get(self.baseURL)
        self.logger.info("********** navigated to baseURL **********")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Validated Title Successfully **********")
        else:
            self.driver.save_screenshot("Screenshots/" + "test_homePageTitle.png")  # Step 4 of Documentation
            self.driver.close()
            self.logger.error("********** Title Validation Failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUpFixture):
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = setUpFixture
        self.driver.get(self.baseURL)
        self.logger.info("********** Navigated to baseURL ************************************")

        # creating object of class LoginPage and passing driver reference in the constructor
        self.lp = LoginPage(self.driver)
        self.logger.info("********** Received driver reference in LoginPage(self.driver) **********")
        self.lp.setUserName(self.username)
        self.logger.info("********** Entered Username **********")
        self.lp.setPassword(self.password)
        self.logger.info("********** Entered Password **********")
        self.lp.clickLogin()
        self.logger.info("********** Clicked Login Button **********")
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********** Title Validation Passed **********")
        else:
            self.driver.save_screenshot("Screenshots/" + "test_login.png")  # Step 4 of Documentation
            self.driver.close()
            self.logger.error("********** Title Validation Failed **********")
            assert False

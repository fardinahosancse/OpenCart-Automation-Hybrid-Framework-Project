import time
import pytest

from Pages.OpenCart_Login import OpenCart_Login_Page
from Utility.configReader import readConfig as rc
from Pages.HomePage import OpenCart_Home_Page
from Pages.OpenCartBasePage import OpenCart
from TestCases.Distribue import Distribute
from Utility import dataProvider
import logging
from Utility.LogUtil import Logger

log = Logger(__name__, logging.INFO)


# @pytest.mark.skip
class Test_Login(Distribute):

    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login", "../Excel/Registration.xlsx"))
    def test_Login_Using_valid_data(self, email, password, get_browser):
        driver = get_browser
        print("Test_Login_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()
        print("Page Title: ", title)

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login(email, password)
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "My Account"
            Unexpected = "Account Login"

            if Login_success_title == Expected:
                assert Login_success_title == Expected, "Login Failed:Try Use different Mail and password"
                log.logger.info("Expected: Successful Login")
            elif Login_success_title == Unexpected:
                assert Login_success_title == Unexpected, "Login Successful"
                log.logger.info("Expected:Successful Login,but it Stays in Login Page")

    def test_Login_Using_no_data(self,get_browser):
        driver = get_browser
        print("Test_Login_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()
        print("Page Title: ", title)

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login("","")
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "Account Login"
            Unexpected = "My Account"


            if Login_success_title == Expected:
                assert Login_success_title == Expected, "Login Successfull"
                log.logger.info("Expected: Unsuccessful Login")
            elif Login_success_title != Unexpected:
                assert Login_success_title == Unexpected, "Login UnSuccessful"
                log.logger.info("Expected:Unsuccessful Login,but It Logged In")

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


@pytest.mark.skip
class Test_Login(Distribute):

    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login-valid", "../Excel/Registration.xlsx"))
    def test_Login_Using_valid_data(self, email, password, get_browser):
        driver = get_browser
        print("test_Login_Using_valid_data_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login(email, password)
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "My Account"
            assert Login_success_title == Expected, f"Login Failed,Current Page :{Login_success_title}"


    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login-invalid", "../Excel/Registration.xlsx"))
    def test_Login_Using_invalid_data(self, email, password, get_browser):
        driver = get_browser
        print("test_Login_Using_invalid_data_Started------")

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
            Expected = "Account Login"
            assert Login_success_title == Expected, f"Unexpected Login Occurs::{Login_success_title}"

    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login-valid", "../Excel/Registration.xlsx"))
    def test_Login_leaving_email_address(self, email, password, get_browser):
        driver = get_browser
        print("test_Login_leaving_email_address_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()
        print("Page Title: ", title)

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login("", password)
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "Account Login"
            assert Login_success_title == Expected, f"Unexpected Login Occurs::{Login_success_title}"

    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login-valid", "../Excel/Registration.xlsx"))
    def test_Login_leaving_password(self, email, password, get_browser):
        driver = get_browser
        print("test_Login_leaving_password_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()
        print("Page Title: ", title)

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login(email, "")
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "Account Login"
            assert Login_success_title == Expected, f"Unexpected Login Occurs::{Login_success_title}"

    def test_Login_Using_no_data(self, get_browser):
        driver = get_browser
        print("test_Login_Using_no_data_Started------")

        # Declaration
        home = OpenCart_Home_Page(driver)
        login = OpenCart_Login_Page(driver)
        Openart = OpenCart(driver)

        # Get Title From Home to ensure we are in right page
        title = Openart.get_page_title()
        print("Page Title: ", title)

        # Login Execution
        if "Your Store" == title:
            home.go_to_Login().do_Login("", "")
            # Check Login Success by Comparing we are in new page that welcome new user
            Login_success_title = Openart.get_page_title()
            print("My Account: ", Login_success_title)
            Expected = "Account Login"


            # Objective : Login Fail if Inputs are blank
            assert Login_success_title == Expected, f"Login Occurs :{Login_success_title}"


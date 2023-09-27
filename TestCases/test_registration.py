import time
import pytest
from Utility.configReader import readConfig as rc
from Pages.HomePage import OpenCart_Home_Page
from Pages.OpenCartBasePage import OpenCart
from TestCases.Distribue import Distribute
from Utility import dataProvider
import logging
from Utility.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Register(Distribute):

    @pytest.mark.parametrize("firstname,lastname,email,password",
                             dataProvider.get_data("Registration-valid", "../Excel/Registration.xlsx"))
    def test_registration_with_valid_data(self, firstname, lastname, email, password,get_browser):
        driver = get_browser
        print("Test_registration_with_valid_data_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()
        if "Your Store" == title:
            home.go_to_Register().Fill_Registration_Form(firstname, lastname, email, password)
            time.sleep(2)
            Registration_success_title = Openart.get_page_title()
            Expected="Your Account Has Been Created!"
            assert Registration_success_title == Expected, f"Registration Failed,Current Page {Registration_success_title}"
        else:
            print("Element Not Found")




    @pytest.mark.parametrize("firstname,lastname,email,password",
                             dataProvider.get_data("Registration-invalid", "../Excel/Registration.xlsx"))
    def test_registration_with_repeated_mail(self, firstname, lastname, email, password,get_browser):
        driver = get_browser
        print("Test_registration_with_valid_data_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()
        if "Your Store" == title:
            home.go_to_Register().Fill_Registration_Form(firstname, lastname, email, password)
            time.sleep(2)
            Registration_success_title = Openart.get_page_title()
            Expected="Register Account"
            assert Registration_success_title == Expected, f"Unexpected Registration Occured::{Registration_success_title}"
        else:
            print("Element Not Found")

    def test_registration_with_no_input(self, get_browser):
        driver = get_browser
        print("test_registration_with_no_input_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()  # Opening Page Title

        if "Your Store" == title:  # Comparing Title to check we are in Opening page or not
            home.go_to_Register().Fill_Registration_Form("", "", "", "")  # Registration Form Fill
            time.sleep(2)
            Registration_Page_Title = Openart.get_page_title()  # Check The current page tile to detect Register Successfull or not
            Expected_Result = "Register Account"
            assert Registration_Page_Title == Expected_Result, f"Unexpected Registration Occured::{Registration_Page_Title}"

        else:
            print("Failed to Detect HomePage")

    @pytest.mark.parametrize("firstname,lastname,email,password",
                             dataProvider.get_data("Registration-valid", "../Excel/Registration.xlsx"))
    def test_registration_leaving_privacy_agreement_toggle(self,firstname, lastname, email, password,get_browser):
        driver = get_browser
        print("test_registration_leaving_privacy_agreement_toggle_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()
        if "Your Store" == title:
            home.go_to_Register().Fill_Registration_Form_without_privacy_agreement(firstname, lastname, email, password)
            time.sleep(2)
            Registration_Page_Title = Openart.get_page_title()  # Check The current page tile to detect Register Successfull or not
            Expected_Result = "Register Account"
            assert Registration_Page_Title == Expected_Result, f"Unexpected Registration Occured::{Registration_Page_Title}"
        else:
            print("Element Not Found")



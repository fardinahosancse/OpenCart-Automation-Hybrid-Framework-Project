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


@pytest.mark.skip
class Test_Register(Distribute):

    @pytest.mark.parametrize("firstname,lastname,email,password",
                             dataProvider.get_data("Registration", "../Excel/Registration.xlsx"))
    def test_registration_with_valid_data(self, firstname, lastname, email, password, get_browser):
        driver = get_browser
        print("Test_registration_with_valid_data_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()
        if "Your Store" == title:
            home.go_to_Register().Fill_Registration_Form(firstname, lastname, email, password)
            time.sleep(2)
            Registration_success_title = Openart.get_page_title()

            # Logic for Handling Same Repeated Email
            if Registration_success_title == "Your Account Has Been Created!":
                log.logger.info("Expected: Successful Register")
                assert Registration_success_title == "Your Account Has Been Created!", "Register Unsuccessful"
            elif Registration_success_title == "Register Account":
                log.logger.info("Expected: Unsuccessful Register")
                assert Registration_success_title == "Register Account", "Register Successful"
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
            Unexpected_Result = "Your Account Has Been Created!"


            if Registration_Page_Title == Expected_Result:
                log.logger.info("Expected: Unsuccessful Register")
                assert Registration_Page_Title == Expected_Result, "Register Successful"
            elif Registration_Page_Title == Unexpected_Result:
                log.logger.info("Expected: Unsuccessful Register:Bug")
                assert Registration_Page_Title == Unexpected_Result, "Register Unsuccessful"
        else:
            print("Failed to Detect HomePage")

    @pytest.mark.parametrize("firstname,lastname,email,password",
                             dataProvider.get_data("Registration", "../Excel/Registration.xlsx"))
    def test_registration_leaving_privacy_agreement_toggle(self, firstname, lastname, email, password, get_browser):
        driver = get_browser
        print("test_registration_leaving_privacy_agreement_toggle_Started------")
        home = OpenCart_Home_Page(driver)  # Use get_browser here
        Openart = OpenCart(driver)  # Use get_browser here
        title = Openart.get_page_title()
        if "Your Store" == title:
            home.go_to_Register().Fill_Registration_Form_without_privacy_agreement(firstname, lastname, email, password)
            time.sleep(2)
            Registration_success_title = Openart.get_page_title()

            # Logic for Handling Same Repeated Email
            if Registration_success_title == "Register Account":
                log.logger.info("Expected: Unsuccessful Register")
                assert Registration_success_title == "Register Account", "Register Successful"
            elif Registration_success_title == "Your Account Has Been Created!":
                log.logger.info("Unexpected: Successfully Register: Bug")
                assert Registration_success_title == "Your Account Has Been Created!", "Register Unsuccessful"
        else:
            print("Element Not Found")

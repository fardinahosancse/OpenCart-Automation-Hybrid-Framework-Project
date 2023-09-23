import time

from Pages.BasePage import BaseFather
from Pages.OpenCart_Login import OpenCart_Login_Page
from Pages.OpenCart_Register import OpenCart_Register_Page


class OpenCart_Home_Page(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

    # Searching
    def search(self, data):
        print("------------Search-----------")
        self.type_on("home_search_field_xpath", data)
        self.click("home_search_button_xpath")

    def get_status_search_valid(self):
        text = self.get_text_from_element("home_search_product_title_xpath")
        return text

    def get_status_search_invalid(self):
        text = self.get_text_from_element("home_search_product_no_result_xpath")
        return text




    def product_title(self):
        text = self.get_text_from_element("prduct_cart_product_title")


    # Responsible For Navigating to Register Page
    def go_to_Register(self):
        print("-------Navigating To Rgistration Page---------")
        self.click("my_account_xpath")
        self.click("do_Register_xpath")
        return OpenCart_Register_Page(self.driver)

    # Responsible For Navigating to Login Page
    def go_to_Login(self):
        print("-------Navigating To Login Page---------")
        self.click("my_account_xpath")
        self.click("do_Login_xpath")
        return OpenCart_Login_Page(self.driver)

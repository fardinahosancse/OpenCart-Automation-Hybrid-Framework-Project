from Pages.BasePage import BaseFather
from Pages.OpenCart_Login import OpenCart_Login_Page
from Pages.OpenCart_Register import OpenCart_Register_Page


class OpenCart_Home_Page(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

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

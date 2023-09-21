import time

from Pages.BasePage import BaseFather
from Pages.OpenCartBasePage import OpenCart


class OpenCart_Register_Page(BaseFather):

    def __init__(self, driver):
        super().__init__(driver)

    def Fill_Registration_Form(self,firstname,lastname,email,password):
        print("-------Filling Registration Form---------")
        self.type_on("reg_first_name_xpath",firstname)
        self.type_on("reg_last_name_xpath",lastname)
        self.type_on("reg_email_xpath",email)
        self.type_on("reg_password_xpath",password)
        self.checkbox("reg_read_agree_xpath")
        self.click("reg_continue_xpath")
        time.sleep(5)

    def Fill_Registration_Form_without_privacy_agreement(self,firstname,lastname,email,password):
        print("-------Filling Registration Form---------")
        self.type_on("reg_first_name_xpath",firstname)
        self.type_on("reg_last_name_xpath",lastname)
        self.type_on("reg_email_xpath",email)
        self.type_on("reg_password_xpath",password)
        self.click("reg_continue_xpath")
        time.sleep(5)














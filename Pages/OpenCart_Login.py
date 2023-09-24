import time

from Pages.BasePage import BaseFather



class OpenCart_Login_Page(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)


    def do_Login(self,email,password):
        print("-------Filling Login ---------")
        self.type_on("log_email_xpath",email)
        self.type_on("log_password_xpath",password)
        self.click("log_login_xpath")
        time.sleep(3)
        return  self
    def go_to_home(self):
        self.click("go_to_home_xpath")






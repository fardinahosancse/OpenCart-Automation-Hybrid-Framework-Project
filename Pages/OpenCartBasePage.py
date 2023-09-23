from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Pages.BasePage import BaseFather
from Utility import configReader
import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)

class OpenCart(BaseFather):
    def __init__(self,driver):
        super().__init__(driver)

#---------------------Custom----------------------------
    def get_RegSuccess_Alert(self):
        text=self.get_title("reg_success_xpath")
        return text

    def get_LogSuccess_Alert(self):
        text=self.get_title("log_success_page_xpath")
        return text

    def log_page_title(self):
        text = self.get_title("log_page_title_xpath")
        return text

    def log_page_success_title(self):
        text = self.get_title("log_success_page_xpath")
        return text

    def get_page_title(self):
        return self.driver.title


#----------------------Default Catcher-------------------

    def alert_text(self):
        Alert=self.driver.switch_to.alert
        AlertText =Alert.text
        return AlertText

    def ScrollDown(self):
        self.driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)




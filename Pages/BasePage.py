from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utility import configReader as conf
import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.alert import Alert

class BaseFather:
    def __init__(self,driver):
        self.driver = driver

    def click(self, syntax):
        if syntax.endswith("_xpath"):
            try:
                # Create a WebDriverWait instance
                wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

                # Use WebDriverWait to wait for the element to be clickable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, conf.readConfig("locatorsData", syntax))))

                # Click the element
                element.click()
                log.logger.info("Clicked on the element with XPath: " + syntax)

            except Exception as e:
                log.logger.error(f"Error clicking on element with XPath {syntax}: {str(e)}")
        else:
            log.logger.warning(f"Invalid syntax: {syntax}")




    def type_on(self,syntex,syntex_value):
        if str(syntex).endswith("_xpath"):
            self.driver.find_element(By.XPATH,conf.readConfig("locatorsData",syntex)).send_keys(syntex_value)
        log.logger.info(">Typing on Input: " + str(syntex) + "," +str(syntex_value))

    def select(self,syntex,selection_value):
        if str(syntex).endswith("_xpath"):
            Select(self.driver.find_element(By.XPATH,conf.readConfig("locatorsData",syntex))).select_by_value(selection_value)
        log.logger.info(">Selecting : " + str(syntex) + "," + str(selection_value))

    def mousehover(self,syntex):
        configLoader = conf.readConfig("locatorsData",syntex)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,configLoader)).perform()
        log.logger.info(">Mouse Hover : " + str(syntex))

    def get_title(self, syntax):
        if str(syntax).endswith("_xpath"):
            wait = WebDriverWait(self.driver, 10)
            success_title_element = wait.until(
                EC.visibility_of_element_located((By.XPATH, conf.readConfig("locatorsData", syntax))))

            title_text = success_title_element
            return title_text

    def checkbox(self, syntex):
        if str(syntex).endswith("_xpath"):
            checkbox_element=self.driver.find_element(By.XPATH, conf.readConfig("locatorsData", syntex))
            if not checkbox_element.is_selected():  # Check if the checkbox is not already selected
                checkbox_element.click()

        log.logger.info(">Clicking on a Element: " + str(syntex))

    def get_text_from_element(self, syntax):
        if syntax.endswith("_xpath"):
            try:
                # Create a WebDriverWait instance
                wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

                # Use WebDriverWait to wait for the element to be clickable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, conf.readConfig("locatorsData", syntax)))).text

                # Click the element
                return element

            except Exception as e:
                log.logger.error(f"Error Findih on element with XPath {syntax}: {str(e)}")
        else:
            log.logger.warning(f"Invalid syntax: {syntax}")







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
class Test_Search(Distribute):

    def test_search_with_valid_product_name(self, get_browser):
        # Driver Initialization
        driver = get_browser
        home = OpenCart_Home_Page(driver)

        # Execution
        home.search("iPhone")

        # Assertion  # Expected : "iPhone" # Status : Search Result will show
        result = home.get_status_search_valid()
        assert result == "iPhone", f"Search Failed:: {result},Expected: 'iPhone' "
        print(f" {result} == 'iPhone' ")

    def test_search_with_invalid_product_name(self, get_browser):
        # Driver Initialization
        driver = get_browser
        home = OpenCart_Home_Page(driver)

        # Execution
        home.search("Miao")
        expected = "There is no product that matches the search criteria."

        # Assertion  # Expected : "No Product" # Status : Search Result will not show
        result = home.get_status_search_invalid()
        assert result == expected, f"Unexpected Search Occured"
        print(f" {result} == {expected}")

    def test_search_with_leaving_blank_product_name(self, get_browser):
        # Driver Initialization
        driver = get_browser
        home = OpenCart_Home_Page(driver)

        # Execution
        home.search("")
        expected = "There is no product that matches the search criteria."

        # Assertion  # Expected : "No Product" # Status : Search Result will not show
        result = home.get_status_search_invalid()
        assert result == expected, f"Unexpected Search Occured"
        print(f" {result} == {expected}")

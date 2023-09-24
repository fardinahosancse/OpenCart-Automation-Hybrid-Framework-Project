import pytest

from Pages.HomePage import OpenCart_Home_Page
from TestCases.Distribue import Distribute
from Pages.CheckoutPage import CheckOut
from Utility import dataProvider


class Test_CheckOut(Distribute):
    @pytest.mark.parametrize("firstname,lastname,shipaddress,city,postcode",
                             dataProvider.get_data("Order", "../Excel/Registration.xlsx"))
    @pytest.mark.parametrize("email,password", dataProvider.get_data("Login-valid", "../Excel/Registration.xlsx"))
    def test_order_placement_with_login(self, email, password, firstname, lastname, shipaddress, city, postcode,
                                        get_browser):
        # Initialization
        driver = get_browser
        cart = OpenCart_Home_Page(driver)
        order = CheckOut(driver)

        # Login
        cart.go_to_Login().do_Login(email, password).go_to_home()

        # Product Search & Select
        cart.search("iPhone")
        order.shopping_cart()
        order.checkout(firstname, lastname, shipaddress, city, postcode).OrderProcess()
        success_title=order.get_order_success_info()
        assert success_title == "Your order has been placed!",f"Order Unsuccessful"
        print(success_title," = Your order has been placed!")

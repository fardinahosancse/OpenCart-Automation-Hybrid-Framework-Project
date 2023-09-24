import time

from Pages.BasePage import BaseFather


class CheckOut(BaseFather):

    def __init__(self, driver):
        super().__init__(driver)

    def shopping_cart(self):
        self.click("chk_iphone_product_xpath")
        self.click("chk_iphone_add_cart_xpath")
        time.sleep(1)
        self.click("chk_view_cart_item_xpath")
        self.click("chk_go_to_shopping_cart_xpath")
        time.sleep(2)
        self.click("chk_Shipping_dropdown_xpath")
        time.sleep(2)
        self.select("chk_drop_country_xpath", "18")
        self.select("chk_drop_city_xpath", "324")
        self.type_on("chk_drop_postcde_xpath", "6100")
        time.sleep(2)
        self.click("chk_drop_get_qoute_xpath")
        # popup
        self.click("chk_shipping_flat_rate_xpath")
        self.click("chk_apply_shipping_xpath")
        time.sleep(2)
        self.click("chk_Shipping_dropdown_xpath")
        time.sleep(2)
        self.click("chk_go_to_checkout_xpath")

    def checkout(self, firstname, lastname, shipaddress, city, postcode):
        self.click("chk_selection_xpath")
        self.select("chk_shipping_selection_xpath", "2")
        time.sleep(3)
        return self

    def OrderProcess(self):
        # Shipping Method Selection
        self.click("chk_shipping_method_xpath")
        self.click("chk_shipping_method_continue_xpath")

        # Payment Method Selection
        self.click("chk_payment_method_xpath")
        self.click("chk_payment_method_input_xpath")
        self.click("chk_payment_method_input_continue_xpath")
        self.type_on("chk_comment_order_xpath", "miao")

        # Place Order
        self.click("chk_order_confirm_xpath")
        time.sleep(3)

    def get_order_success_info(self):
        text = self.get_text_from_element("chk_order_successful_xpath")
        return text

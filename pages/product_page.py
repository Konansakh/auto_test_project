from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_item = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_item.click()

    def should_be_successfully_added(self, name):
        assert self.is_element_present(*ProductPageLocators.ADDED_MESSAGE), "Item not added in cart"
        message = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE).text
        assert name == message, "Added not selected book"

    def should_be_basket_total_equal_price(self, price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "Basket total message not appear"
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert price == basket_total_price, f"Basket total price not correct for this one book, expected: {price}, get: {basket_total_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_MESSAGE), \
            "Success message is not disappeared, but should be"

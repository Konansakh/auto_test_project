from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_added_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_ITEMS_LINK), \
            "Some products is in your basket, but should not be"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_LINK), "Your basket is not empty"
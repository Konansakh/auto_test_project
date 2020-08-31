from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def save_original_name_and_price(self):
        self.name = self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_NAME).text
        self.price = self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_PRICE).text

    def return_original_name(self):
        return self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_NAME).text

    def return_original_price(self):
        return self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_PRICE).text
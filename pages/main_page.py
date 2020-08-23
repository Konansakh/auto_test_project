from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def save_original_name_and_price(self):
        self.name = self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_NAME).text
        self.price = self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_PRICE).text

    def return_original_name(self):
        return self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_NAME).text

    def return_original_price(self):
        return self.browser.find_element(*MainPageLocators.ORIGINAL_BOOK_PRICE).text
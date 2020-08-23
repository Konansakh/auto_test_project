from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    original_name = page.return_original_name()
    original_price = page.return_original_price()
    #  page.save_original_name_and_price()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    #  product_page.should_be_successfully_added(page.name)
    #  product_page.should_be_basket_total_equal_price(page.price)
    product_page.should_be_successfully_added(original_name)
    product_page.should_be_basket_total_equal_price(original_price)

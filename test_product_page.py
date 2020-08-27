import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
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

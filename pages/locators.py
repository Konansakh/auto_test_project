from selenium.webdriver.common.by import By


class MainPageLocators():
    ORIGINAL_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ORIGINAL_BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    CREATE_USER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    ADDED_ITEMS_FORM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_FORM = (By.CSS_SELECTOR, "#content_inner>p")

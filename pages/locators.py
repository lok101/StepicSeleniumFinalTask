from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')

    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'div.alertinner')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success div.alertinner strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

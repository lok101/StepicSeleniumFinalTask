from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class RegistrationFormLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    ONE_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    SECOND_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'form#register_form  button')
    EXIT_BUTTON = (By.CSS_SELECTOR, '#logout_link')


class ProductPageLocators:
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')

    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span a.btn-default')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, 'div.alertinner')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success div.alertinner strong')


class BasketPageLocators:
    PRODUCT_BLOCK = (By.CSS_SELECTOR, 'div.basket-title div h2')
    TEXT_TO_EMPTY_BLOCK = (By.CSS_SELECTOR, '#content_inner > p')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

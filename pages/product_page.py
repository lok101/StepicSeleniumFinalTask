from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    # добавить в корзину
    def add_to_basket_page(self):
        self.should_be_add_in_basket_page()
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        login_link.click()

    # проверить добавлено ли в корзину
    def checking_the_basket(self, name_product, price_product):
        self.basket_cost_comparison(price_product)
        self.should_be_product_in_basket(name_product)

    # возвращает имя товара со страницы товара
    def return_name_product(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    # возвращает цену товара со страницы товара
    def return_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    # проверяет наличие кнопки "добавить в корзину"
    def should_be_add_in_basket_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Basket button is not presented"

    # сверяет название товара
    def should_be_product_in_basket(self, name_product):
        banner_text = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert f'{name_product} был добавлен в вашу корзину.' == banner_text

    # сверяет цену
    def basket_cost_comparison(self, price_product):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_product == price_basket

    # вводит "капчу"
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # проверяет, нет ли элемента
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # проверяет, исчезнет ли элемент
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

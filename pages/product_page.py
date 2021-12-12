from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def go_to_basket_page(self):
        self.should_be_basket_button()
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()

    def checking_the_basket(self, name_product, price_product):
        self.basket_cost_comparison(price_product)
        self.should_be_product_in_basket(name_product)

    def return_name_product(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    def return_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_be_product_in_basket(self, name_product):
        banner_text = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert f'{name_product} был добавлен в вашу корзину.' == banner_text

    def basket_cost_comparison(self, price_product):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_product == price_basket

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

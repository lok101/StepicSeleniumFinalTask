from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BLOCK)
        # проверяет, есть ли блок добавленных товаров на странице корзины

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_TO_EMPTY_BLOCK)
        # проверяет, есть ли блок текста, говорящий о том, что корзина пуста

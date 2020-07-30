from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name_added(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def succes_product_adding(self,product_name):
        assert product_name==self.get_product_name_added(),\
            f'Product in basket expected "{product_name}" got "{self.get_product_name_added()}"'

    def basket_price_is_true(self,product_price):
        assert product_price == self.get_basket_price(), \
             f'Basket price expected "{product_price}" got "{self.get_basket_price()}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not disappeared"

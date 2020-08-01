from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    #def should_be_basket_link_in_product(self):
    #    assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Add to basket button is not presented"

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("basket")>0, f'String "{self.browser.current_url}" is not basket url'
        #assert True

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ROW), \
            "Product is presented, but should not be"

    def empty_basket_message_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_EMPTY_BASKET), \
            "Empty basket message not present"

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



    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not disappeared"
        
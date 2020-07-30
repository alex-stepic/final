from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import pytest


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

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  # оборачиваем найденную ссылку с багом
#                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])@

def test_guest_can_add_product_to_basket(browser,link= "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    product_page= ProductPage(browser, link)   # инициализируем ProductPage Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()                      # открываем страницу

    product_page.should_be_basket_link()
    product_name=product_page.get_product_name()
    product_price=product_page.get_product_price()

    product_page.add_to_basket()
    solve_quiz_and_get_code(product_page)

    product_page.succes_product_adding(product_name)
    product_page.basket_price_is_true(product_price)

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    product_page = ProductPage(browser,link)  # инициализируем ProductPage Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу

    product_page.add_to_basket()
    solve_quiz_and_get_code(product_page)

    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser,link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"   ):
    product_page = ProductPage(browser,link)  # инициализируем ProductPage Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу

    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser,link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"):
    product_page = ProductPage(browser,link)  # инициализируем ProductPage Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу

    product_page.add_to_basket()
    solve_quiz_and_get_code(product_page)

    product_page.success_message_is_disappeared()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.empty_basket_message_present()

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM= (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_EMAIL=(By.CSS_SELECTOR,'input[name="registration-email"]')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators ():
    ADD_TO_BASKET= (By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".col-sm-6.product_main h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".col-sm-6.product_main p.price_color")
    PRODUCT_NAME_ADDED=(By.CSS_SELECTOR,"div.container-fluid.page div.page_inner div.alert.alert-success:nth-child(1) .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR,"div.container-fluid.page div.page_inner div.alert.alert-info .alertinner strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,"div.container-fluid.page div.page_inner div.alert.alert-success")

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, 'span a.btn.btn-default[href*="basket"]')
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, 'span a.btn.btn-default[href*="basket_invalid"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators ():
   PRODUCT_ROW = (By.CSS_SELECTOR, ".basket-items .row")
   MESSAGE_IN_EMPTY_BASKET = (By.XPATH,'//p[contains(text(),"basket is empty")]')
   
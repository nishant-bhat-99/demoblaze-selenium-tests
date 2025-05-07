from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    HOME_BUTTON = (By.XPATH, ".//a[text()='Home ']")
    CONTACT_BUTTON = (By.XPATH, ".//a[text()='Contact']")
    ABOUT_US_BUTTON = (By.XPATH, ".//a[text()='About us']")
    CART_BUTTON = (By.XPATH, ".//a[text()='Cart']")
    LOGIN_BUTTON = (By.ID, "login2")
    SIGNUP_BUTTON = (By.XPATH, ".//a[text()='Sign up']")
    CONTACT_POP_UP = (By.ID,"exampleModal")
    ABOUT_US_POP_UP = (By.ID,"videoModal")
    LOGIN_POP_UP = (By.ID,"logInModal")
    SIGNUP_POP_UP = (By.ID,"signInModal")
    CAROUSEL_FIRST_IMAGE = (By.XPATH,".//img[@alt='First slide']")
    CAROUSEL_SECOND_IMAGE = (By.XPATH, ".//img[@alt='Second slide']")
    CAROUSEL_THIRD_IMAGE = (By.XPATH, ".//img[@alt='Third slide']")
    CAROUSEL_NEXT = (By.XPATH,".//a[@class='carousel-control-next']")
    CAROUSEL_PREV = (By.XPATH,".//a[@class='carousel-control-prev']")
    CATEGORY_PHONES_BUTTON = (By.XPATH,".//a[text()='Phones']")
    CATEGORY_LAPTOPS_BUTTON = (By.XPATH,".//a[text()='Laptops']")
    CATEGORY_MONITORS_BUTTON = (By.XPATH,".//a[text()='Monitors']")
    PRODUCTS = (By.XPATH,".//h4[@class='card-title']")
    FIRST_PRODUCT_TITLE = (By.XPATH, "(//h4[@class='card-title'])[1]")
    CONTACT_EMAIL_INPUT = (By.ID,"recipient-email")
    CONTACT_NAME_INPUT = (By.ID,"recipient-name")
    CONTACT_MESSAGE_INPUT = (By.ID,"message-text")
    CONTACT_SEND_MESSAGE_BUTTON = (By.XPATH,"//button[text()='Send message']")
    CONTACT_CLOSE_BUTTON = (By.XPATH,"//button[text()='Close']")
    LOGIN_USERNAME_INPUT = (By.ID,"loginusername")
    LOGIN_PASSWORD_INPUT = (By.ID,"loginpassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH,"//button[text()='Log in']")
    LOGIN_CLOSE_BUTTON = (By.XPATH,"//button[text()='Close']")
    SIGNED_IN_STATUS = (By.ID,"nameofuser")
    SIGNUP_USERNAME_INPUT = (By.ID,"sign-username")
    SIGNUP_PASSWORD_INPUT = (By.ID,"sign-password")
    SIGNUP_SUBMIT_BUTTON = (By.XPATH,"//button[text()='Sign up']")
    SIGNUP_CLOSE_BUTTON = (By.XPATH,"//button[text()='Close']")
    ADD_TO_CART_BUTTON = (By.XPATH,"//a[text()='Add to cart']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='btn btn-success']")


    def button_home(self):
        self.click(self.HOME_BUTTON)
        self.wait_for_element(self.CATEGORY_MONITORS_BUTTON)

    def button_contact(self):
        self.click(self.CONTACT_BUTTON)

    def button_about_us(self):
        self.click(self.ABOUT_US_BUTTON)

    def button_cart(self):
        self.click(self.CART_BUTTON)
        self.wait_for_element(self.PLACE_ORDER_BUTTON)

    def button_login(self):
        self.click(self.LOGIN_BUTTON)

    def button_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def contact_pop_up_open(self):
        element=self.find(self.CONTACT_POP_UP)
        self.wait_for_element(self.CONTACT_POP_UP)
        if element.get_attribute("aria-hidden")=="true":
            return False
        else:
            return True

    def about_us_pop_up_open(self):
        element=self.find(self.ABOUT_US_POP_UP)
        self.wait_for_element(self.ABOUT_US_POP_UP)
        if element.get_attribute("aria-hidden")=="true":
            return False
        else:
            return True

    def login_pop_up_open(self):
        self.wait_for_element(self.LOGIN_POP_UP)
        element=self.find(self.LOGIN_POP_UP)
        if element.get_attribute("aria-hidden")=="true":
            return False
        else:
            return True

    def signup_pop_up_open(self):
        element=self.find(self.SIGNUP_POP_UP)
        self.wait_for_element(self.SIGNUP_POP_UP)
        if element.get_attribute("aria-hidden")=="true":
            return False
        else:
            return True

    def carousel_right(self):
        self.click(self.CAROUSEL_NEXT)

    def carousel_left(self):
        self.click(self.CAROUSEL_PREV)

    def carousel_first_image_check(self):
        self.wait_for_element(self.CAROUSEL_FIRST_IMAGE)
        element=self.find(self.CAROUSEL_FIRST_IMAGE)
        return element.is_displayed()

    def carousel_second_image_check(self):
        self.wait_for_element(self.CAROUSEL_SECOND_IMAGE)
        element=self.find(self.CAROUSEL_SECOND_IMAGE)
        return element.is_displayed()

    def carousel_third_image_check(self):
        self.wait_for_element(self.CAROUSEL_THIRD_IMAGE)
        element=self.find(self.CAROUSEL_THIRD_IMAGE)
        return element.is_displayed()

    def button_category_phones(self):
        self.click(self.CATEGORY_PHONES_BUTTON)
        self.wait_for_first_product_title(self.FIRST_PRODUCT_TITLE,"Samsung galaxy s6")

    def button_category_laptops(self):
        self.click(self.CATEGORY_LAPTOPS_BUTTON)
        self.wait_for_first_product_title(self.FIRST_PRODUCT_TITLE,"Sony vaio i5")

    def button_category_monitors(self):
        self.click(self.CATEGORY_MONITORS_BUTTON)
        self.wait_for_first_product_title(self.FIRST_PRODUCT_TITLE,"Apple monitor 24")

    def category_number_of_products(self):
        return len(self.find_all(self.PRODUCTS))

    def fill_contact_form(self, email, name, message):
        self.wait_for_element(self.CONTACT_POP_UP)
        self.enter_text(self.CONTACT_EMAIL_INPUT, email)
        self.enter_text(self.CONTACT_NAME_INPUT, name)
        self.enter_text(self.CONTACT_MESSAGE_INPUT, message)
        self.click(self.CONTACT_SEND_MESSAGE_BUTTON)

    def fill_login_form(self,username,password):
        self.wait_for_element(self.LOGIN_POP_UP)
        self.enter_text(self.LOGIN_USERNAME_INPUT,username)
        self.enter_text(self.LOGIN_PASSWORD_INPUT,password)
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def check_logged_in(self):
        self.wait_for_element(self.SIGNED_IN_STATUS)
        return self.is_element_visible(self.SIGNED_IN_STATUS)

    def fill_signup_form(self,username,password):
        self.wait_for_element(self.SIGNUP_POP_UP)
        self.enter_text(self.SIGNUP_USERNAME_INPUT,username)
        self.enter_text(self.SIGNUP_PASSWORD_INPUT,password)
        self.click(self.SIGNUP_SUBMIT_BUTTON)

    def open_product_page(self,index):
        self.wait_for_element(self.PRODUCTS)
        element = self.find_all(self.PRODUCTS)
        element[index].click()

    def is_product_page_open(self):
        try:
            self.wait_for_element(self.ADD_TO_CART_BUTTON)
            return self.is_element_present(self.ADD_TO_CART_BUTTON)
        except:
            return False








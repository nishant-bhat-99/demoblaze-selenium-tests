from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(BasePage):
    CART_BUTTON = (By.XPATH, ".//a[text()='Cart']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text()='Add to cart']")
    CART_FIRST_ROW = (By.XPATH,"//tbody[@id='tbodyid']/tr[1]/td")
    CART_FIRST_ROW_DELETE_BUTTON = (By.XPATH,"//tbody[@id='tbodyid']//a")
    CART_ROW_NUMBER = (By.XPATH,"//tbody[@id='tbodyid']/tr/td[1]")
    CART_ROWS = "//tbody[@id='tbodyid']/tr[{}]/td"
    PLACE_ORDER_BUTTON = (By.XPATH,"//button[@class='btn btn-success']")
    NAME_INPUT_FIELD = (By.ID,"name")
    COUNTRY_INPUT_FIELD = (By.ID, "country")
    CITY_INPUT_FIELD = (By.ID, "city")
    CCARD_INPUT_FIELD = (By.ID,"card")
    MONTH_INPUT_FIELD = (By.ID,"month")
    YEAR_INPUT_FIELD = (By.ID,"year")
    PURCHASE_BUTTON = (By.XPATH,"//button[@onclick='purchaseOrder()']")
    CONFIRMATION_OKAY_BUTTON = (By.XPATH,".//button[@class='confirm btn btn-lg btn-primary']")
    PURCHASE_CLOSE_BUTTON = (By.XPATH,"//div[@id='orderModal']//button[text()='Close']")
    PURCHASE_CONFIRMATION = (By.XPATH,".//h2[text()='Thank you for your purchase!']")
    HOME_CHECK = (By.ID, "cat")
    CONFIRMATION_FORM_MODAL = (By.XPATH,"//div[@class='sweet-alert  showSweetAlert visible']")

    def add_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON)
        self.click(self.ADD_TO_CART_BUTTON)

    def verify_add_product(self,name,price,row_no):
        self.wait_for_element(self.CART_FIRST_ROW_DELETE_BUTTON)
        product=self.get_cart_row(row_no)
        return product[1].text.strip()==name and product[2].text.strip()==price

    def delete_product(self):
        self.wait_for_element(self.CART_FIRST_ROW)
        self.click(self.CART_FIRST_ROW_DELETE_BUTTON)
        self.wait_for_product_deletion(self.CART_FIRST_ROW)

    def is_cart_empty(self):
        print (len(self.find_all(self.CART_ROW_NUMBER)))
        return len(self.find_all(self.CART_ROW_NUMBER))==0

    def wait_for_product_deletion(self, row_locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(row_locator))

    def wait_until_cart_empty(self,timeout=10):
        WebDriverWait(self.browser,timeout).until(lambda driver: self.is_cart_empty())

    def get_cart_row(self,row_no):
        locator=(By.XPATH,self.CART_ROWS.format(row_no))
        return self.find_all(locator)

    def button_place_order(self):
        self.wait_for_element(self.PLACE_ORDER_BUTTON)
        self.click(self.PLACE_ORDER_BUTTON)

    def fill_place_order_form(self,name,country,city,ccard,month,year):
        self.wait_for_element(self.NAME_INPUT_FIELD)
        self.enter_text(self.NAME_INPUT_FIELD,name)
        self.enter_text(self.COUNTRY_INPUT_FIELD,country)
        self.enter_text(self.CITY_INPUT_FIELD,city)
        self.enter_text(self.CCARD_INPUT_FIELD,ccard)
        self.enter_text(self.MONTH_INPUT_FIELD,month)
        self.enter_text(self.YEAR_INPUT_FIELD,year)
        self.click(self.PURCHASE_BUTTON)

    def check_order_confirmation(self):
        self.wait_for_element(self.PURCHASE_CONFIRMATION)
        return self.is_element_visible(self.PURCHASE_CONFIRMATION)

    def button_purchase_form_close(self):
        self.wait_for_element(self.PURCHASE_CLOSE_BUTTON)
        self.click(self.PURCHASE_CLOSE_BUTTON)
        WebDriverWait(self.browser, 10).until_not(EC.visibility_of_element_located(self.PURCHASE_BUTTON))
        return not self.is_element_visible(self.PURCHASE_BUTTON)

    def button_confirmation_ok(self):
        self.wait_for_element(self.CONFIRMATION_FORM_MODAL)
        self.click(self.CONFIRMATION_OKAY_BUTTON)
        self.wait_for_element(self.HOME_CHECK)





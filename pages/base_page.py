from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,browser):
        self.browser=browser
        self.wait = WebDriverWait(browser, 10)

    def find(self,locator):
        return self.browser.find_element(*locator)

    def find_all(self, locator):
        return self.browser.find_elements(*locator)

    def find_all_inside(self, parent, locator):
        return parent.find_elements(*locator)

    def click(self,locator):
        self.find(locator).click()

    def enter_text(self,locator,text):
        self.find(locator).send_keys(text)

    def is_element_present(self,locator):
        if self.find(locator) is not None:
            return True
        else:
            return False

    def is_element_visible(self, locator):
        return self.find(locator).is_displayed()

    def wait_for_first_product_title(self, locator, expected_text, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert(self, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())



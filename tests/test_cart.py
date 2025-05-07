from pages.cart_page import CartPage
from pages.home_page import HomePage
import time

def test_cart_add_product(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(3)
    cart.add_to_cart()
    alert = home.wait_for_alert()
    assert alert.text == "Product added"
    alert.accept()

def test_cart_verify_product_added(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(3)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    assert cart.verify_add_product("Samsung galaxy s7", "800",1)

def test_cart_delete_product(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(4)
    cart.add_to_cart()
    home.button_cart()
    assert cart.verify_add_product("Iphone 6 32gb","790",1)
    cart.delete_product()
    cart.wait_until_cart_empty()
    assert cart.is_cart_empty()

def test_add_multiple_product(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(3)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    browser.get("https://www.demoblaze.com")
    home.open_product_page(1)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    home.wait_for_element(cart.CART_FIRST_ROW_DELETE_BUTTON)
    assert cart.verify_add_product("Samsung galaxy s7","800",1)
    assert cart.verify_add_product("Nokia lumia 1520","820",2)



def test_delete_multiple_product(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    browser.get("https://www.demoblaze.com")
    home.open_product_page(4)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.delete_product()
    cart.delete_product()
    assert cart.is_cart_empty()

def test_place_order(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.button_place_order()
    cart.fill_place_order_form("Ezio","Italy","Rome","123456789","February","1999")
    assert cart.check_order_confirmation()

def test_close_place_order_form(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.button_place_order()
    assert cart.button_purchase_form_close()

def test_accept_order_confirmation(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.button_place_order()
    cart.fill_place_order_form("Ryan","America","Scranton","123456789","February","1999")
    cart.button_confirmation_ok()
    assert browser.current_url=="https://www.demoblaze.com/index.html"

def test_place_order_fails_with_empty_form(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.button_place_order()
    cart.fill_place_order_form("","","","","","")
    alert = home.wait_for_alert()
    assert alert.text=="Please fill out Name and Creditcard."
    alert.accept()

def test_order_confirmation_screenshot(browser):
    browser.get("https://www.demoblaze.com")
    home = HomePage(browser)
    cart = CartPage(browser)
    home.open_product_page(5)
    cart.add_to_cart()
    home.wait_for_alert().accept()
    home.button_cart()
    cart.button_place_order()
    cart.fill_place_order_form("Jurgen","Germany","Dortmund","123456789","February","1999")
    browser.save_screenshot("confirmation_order.png")



    #empty field and save screenshot


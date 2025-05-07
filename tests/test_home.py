from pages.home_page import HomePage

def test_home_navigation(browser):
    browser.get("https://www.demoblaze.com/")
    home=HomePage(browser)
    home.button_home()
    assert browser.current_url=="https://www.demoblaze.com/index.html"

def test_contact_navigation(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_contact()
    assert home.contact_pop_up_open()

def test_about_us_navigation(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_about_us()
    assert home.about_us_pop_up_open()

def test_cart_navigation(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_cart()
    assert browser.current_url=="https://www.demoblaze.com/cart.html"

def test_login_navigation(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_login()
    assert home.login_pop_up_open()

def test_signup_navigation(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_signup()
    assert home.signup_pop_up_open()

def test_image_carousel(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    assert home.carousel_first_image_check()
    home.carousel_right()
    assert home.carousel_second_image_check()
    home.carousel_right()
    assert home.carousel_third_image_check()

def test_categories_check(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_category_phones()
    assert home.category_number_of_products()==7
    home.button_category_laptops()
    assert home.category_number_of_products()==6
    home.button_category_monitors()
    assert home.category_number_of_products()==2

def test_contact_submit_form(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_contact()
    home.fill_contact_form("test@selenium.com","Nishant","Test message")
    alert = home.wait_for_alert()
    assert alert.text == "Thanks for the message!!"
    alert.accept()

def test_login_wrong_username(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_login()
    home.fill_login_form("wrong_username","password")
    alert = home.wait_for_alert()
    assert alert.text == "User does not exist."
    alert.accept()

def test_login_wrong_password(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_login()
    home.fill_login_form("username","wrong_password")
    alert = home.wait_for_alert()
    assert alert.text == "Wrong password."
    alert.accept()

def test_login_correct_credentials(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_login()
    home.fill_login_form("username","password")
    assert home.check_logged_in()

def test_signup_new_account(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_signup()
    home.fill_signup_form("new_tester_1999","password")
    alert = home.wait_for_alert()
    assert alert.text == "Sign up successful."
    alert.accept()
    home.button_login()
    home.fill_login_form("new_tester_1999","password")
    assert home.check_logged_in()

def test_signup_empty_fields(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.button_signup()
    home.fill_signup_form("","")
    alert = home.wait_for_alert()
    assert alert.text == "Please fill out Username and Password."

def test_product_open(browser):
    browser.get("https://www.demoblaze.com")
    home=HomePage(browser)
    home.open_product_page(0)
    assert home.is_product_page_open()
    browser.back()
    home.button_category_laptops()
    home.open_product_page(1)
    assert home.is_product_page_open()










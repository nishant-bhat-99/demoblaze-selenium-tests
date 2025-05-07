import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()  # Create an options object
    chrome_options.add_argument("--start-maximized")  # Start browser maximized

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Pass options
    yield driver
    driver.quit()

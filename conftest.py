from ssl import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    options = ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()

@pytest.fixture()
def browser2():
    options = FirefoxOptions()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()
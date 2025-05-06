from selenium.webdriver.common.by import By
from pages.mainpage import MainPage
from pages.about import AboutPage
from pages.whytouse import WhyToUse


def test_main_about_is_present(browser):
    main_page=MainPage(browser)
    main_page.open()
    assert main_page.find_about().is_displayed()

def test_main_about_is_present_2(browser2):
    main_page=MainPage(browser2)
    main_page.open()
    assert main_page.find_about().is_displayed()

def test_main_about_is_opened(browser):
    main_page=MainPage(browser)
    main_page.open()
    main_page.click_about()
    browser.implicitly_wait(3)
    about=AboutPage(browser)
    about.check_title_advanced_is_present()

def test_main_why_to_use_is_present(browser):
    main_page=MainPage(browser)
    main_page.open()
    assert main_page.find_why_to_use().is_displayed()

def test_main_why_to_use_is_opened(browser):
     main_page = MainPage(browser)
     main_page.open()
     main_page.click_why_to_use()
     why_to_use = WhyToUse(browser)
     why_to_use.check_title_why_to_use()

def test_main_dropdown_how_it_works_is_present(browser):
    main_page=MainPage(browser)
    main_page.open()
    assert main_page.find_dropdown_why_to_use().is_displayed()


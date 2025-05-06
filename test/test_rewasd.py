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
    assert browser.current_url == "https://www.rewasd.com/advanced-controller-mapping"

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

def test_button_buy_now_on_header_is_present(browser):
    main_page=MainPage(browser)
    main_page.open()
    assert main_page.find_button_buy_now_on_header().is_displayed()

def test_button_buy_now_on_header_is_working(browser):
    main_page=MainPage(browser)
    main_page.open()
    main_page.find_button_buy_now_on_header().click()
    assert browser.current_url == "https://www.rewasd.com/checkout"

def test_button_download_on_header_is_showed(browser):
    main_page=MainPage(browser)
    main_page.open()
    assert main_page.find_button_download_on_header().is_displayed()

def test_button_download_on_header_is_call_two_items_on_dropdown(browser):
    main_page=MainPage(browser)
    main_page.open()
    main_page.click_button_download_on_header()
    assert len(main_page.check_download_on_header_is_opening_dropdown()) ==2

def test_button_download_in_dropdown_on_header_is_clicking(browser):
    main_page=MainPage(browser)
    main_page.open()
    main_page.click_button_download_on_header()
    main_page.click_on_dropdown_items_download_on_header_x64()
    main_page.click_button_download_on_header()
    main_page.click_on_dropdown_items_download_on_header_arm()





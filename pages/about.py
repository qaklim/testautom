from selenium.webdriver.common.by import By

class AboutPage:

    def __init__(self, browser):
        self.browser = browser


    def check_title_advanced_is_present(self):
        page_title = self.browser.find_element(By.XPATH, "//span[text()='Advanced '] ")
        assert page_title.is_displayed()
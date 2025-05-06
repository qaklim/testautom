from selenium.webdriver.common.by import By

class WhyToUse:
    def __init__(self, browser):
        self.browser = browser

    def check_title_why_to_use(self):
        title = self.browser.find_element(By.XPATH, "//span[text()='Why to use reWASD as a keyboard, '] ")
        assert title.is_displayed()
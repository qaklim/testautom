from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def open (self):
        self.browser.get("https://rewasd.com")

    def click_about (self):
        about = self.browser.find_element(By.XPATH, "//a[text()='About']")
        about.click()

    def find_about(self):
        about = self.browser.find_element(By.XPATH, "//a[text()='About']")
        return about

    def find_why_to_use(self):
        why_to_use = self.browser.find_element(By.XPATH, "//a[text()='Why to Use']")
        return why_to_use

    def click_why_to_use(self):
        why_to_use = self.browser.find_element(By.XPATH, "//a[text()='Why to Use']")
        why_to_use.click()

    def find_dropdown_why_to_use(self):
        dropdown_how_it_works = self.browser.find_element(By.XPATH, "//div[text()='How It Works']")
        return dropdown_how_it_works
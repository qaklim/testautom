from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Membership:
    def __init__(self, browser):
        self.browser = browser

    def check_title(self):
        membership_title = self.browser.find_element(By.XPATH, "//h1[text()='Membership']")
        return membership_title

    def click_on_user_ico(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='account-link btn btn-sm btn-navbar ripple dropdown-toggle btn-default']")))
        sign = self.browser.find_element(By.XPATH, "//div[@class='account-link btn btn-sm btn-navbar ripple dropdown-toggle btn-default']")
        sign.click()

    def click_on_sign_out(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Sign Out']")))
        sign = self.browser.find_element(By.XPATH, "//a[text()='Sign Out']")
        sign.click()